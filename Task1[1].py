import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

# Create a Basemap instance
plt.figure(figsize=(10, 8))
m = Basemap(projection='merc',  # Using Mercator projection
            llcrnrlat=-60, urcrnrlat=60,  # Lower and upper latitude limits
            llcrnrlon=-180, urcrnrlon=180,  # Lower and upper longitude limits
            resolution='c')  # Coastline resolution

# Draw map features
m.drawcoastlines()
m.drawcountries()

# Sample data: latitudes, longitudes, and intensity
latitudes = np.random.uniform(-60, 60, 100)
longitudes = np.random.uniform(-180, 180, 100)
intensity = np.random.rand(100)  # Random intensity values

# Project data points to map projection coordinates
x, y = m(longitudes, latitudes)  # Corrected variable names
sc = m.scatter(x, y, c=intensity, cmap='hot', alpha=0.7)  # Scatter plot with intensity

# Colorbar
cbar = plt.colorbar(sc)  # Fixed syntax for colorbar
cbar.set_label('Intensity')

plt.title("Geographical Heatmap Example")
plt.show()
