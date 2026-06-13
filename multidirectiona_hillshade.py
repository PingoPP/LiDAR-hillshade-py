import os 
import numpy as np
import rasterio  
import matplotlib.pyplot as plt 
from matplotlib_scalebar.scalebar import ScaleBar

dtm_data = rasterio.open(os.path.join(r"dowland you .tif data")) #<--- dowland .tif data

#I recommend that for better knowing about .tif data
print("X:", dtm_data.bounds.left, "to", dtm_data.bounds.right)
print("Y:", dtm_data.bounds.bottom, "to", dtm_data.bounds.top)
print("Z:", dtm_data.read(1).min(), "to", dtm_data.read(1).max())


#basic hillshade with bruh formula
def hillshade(dtm, azimuth=350, angle_altitude=45, cellsize=0.5):

    azimuth_rad = np.radians(azimuth)
    altitude_rad = np.radians(angle_altitude)

    cellsize_x = dtm.res[0]
    cellsize_y = dtm.res[1]

    x, y = np.gradient(dtm.read(1), cellsize_x, cellsize_y)
    slope = np.pi * 2 - np.arctan(np.sqrt(x*x + y*y)) #you change slope like (x**2 + y**2)
    aspect = np.arctan2(-x, y)
  
#here you can combine by sin [sine] and cos [cosine]...Pure math!
    shaded = (       
        np.sin(altitude_rad) *
        np.cos(altitude_rad) +
        np.sin(slope) *
        np.cos((azimuth_rad - np.pi/2.0) - aspect)  
    )
    return shaded

# heart of code oh yeah!!!
def multidirectional_hillshade(dtm):
  #  #azimuth_color [r = red, g = green, b = blue] = [sun direction, R, G, B]
    azimuth_r = [315, 247, 10, 10]
    azimuth_g = [10, 22, 230, 50]
    azimuth_b = [45, 19, 90, 230]

    r = np.mean([hillshade(dtm, azimuth=az) for az in azimuth_r], axis=0)
    g = np.mean([hillshade(dtm, azimuth=az) for az in azimuth_g], axis=0)
    b = np.mean([hillshade(dtm, azimuth=az) for az in azimuth_b], axis=0)

    def norm(arr):
        return (arr - arr.min()) / (arr.max() - arr.min())
    
    rgb = np.dstack((norm(r), norm(g), norm(b)))
    return rgb

#north arrow
ax.annotate(
    'N',
    xy=(0.92, 0.18),
    xytext=(0.92, 0.08),
    arrowprops=dict(
        facecolor='black',
        edgecolor='white',
        width=4,
        headwidth=10
    ),
    ha='center',
    fontsize=18,
    fontweight='bold',
    xycoords=ax.transAxes
)
#scale bar
scalebar = ScaleBar(1, units="m", location="lower left")
ax.add_artist(scalebar)

plt.show()
