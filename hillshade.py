import os 
import numpy as np
import rasterio as rio 
import matplotlib.pyplot as plt 

dtm_data = rio.open(os.path.join("data","upload document .tif"))

ext = [
    dtm_data.bounds.left,
    dtm_data.bounds.right,
    dtm_data.bounds.bottom,
    dtm_data.bounds.top
]

def hillshade(dtm, azimuth=350, angle_altitude=45, cellsize=0.5):
    azimuth = 360.0 - azimuth

    azimuth_rad = np.radians(azimuth)
    altitude_rad = np.radians(angle_altitude)

    cellsize_x = dtm.res[0]
    cellsize_y = dtm.res[1]

    x, y = np.gradient(dtm.read(1), cellsize_x, cellsize_y)
    slope = np.pi * 2 - np.arctan(np.sqrt(x*x + y*y))
    aspect = np.arctan2(-x, y)


    shaded = (
        np.cos(altitude_rad) +
        np.cos(altitude_rad) *
        np.sin(slope) *
        np.sin((azimuth_rad - np.pi/2.0) - aspect)
    )

    return shaded

hs = hillshade(dtm_data, 350, 45, 0.5)
fig, ax = plt.subplots(figsize=(5, 5))
im = ax.imshow(hs, cmap="Greys", extent=ext)
plt.colorbar(im, ax=ax)
ax.set_title("Hillshade")
plt.show()

