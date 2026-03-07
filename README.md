The implemented Python hillshade was compared with the classic hillshade from the Relief Visualization Toolbox (RVT) in QGIS. The goal was to verify whether the Python implementation produces the same results when using identical parameters.

Both visualizations were generated with:

          -	azimuth = 350°
          -	altitude angle = 45°


<figure>
    <img width="1798" height="911" alt="lidar-hillshade" src="https://github.com/user-attachments/assets/bb0c2dd0-0e9d-4436-816c-8ce56ecba810" />
    <figcaption>Figure 1: Left side: RVT classic Hillshade (QGIS). Meanwhile on the right side: Python hillshade implementation (this repository).</figcaption>
</figure>
<br><br>

A noticeable difference appears on the shaded (darker) slopes. The RVT result applies additional filtering, which produces a smoother terrain representation and reduces very dark areas. In contrast, the Python implementation preserves stronger shadow contrast. Because of this, subtle terrain features may be less visible, which can be important for archaeological interpretation.
