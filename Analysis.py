from datetime import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
import datetime
import numpy as np

# Build list of stations
stations = build_station_list()
N = 5
level_values = stations_highest_rel_level(stations, N)
# Update latest level data for all stations
update_water_levels(stations)
for stations in level_values:
    dt = 2
    dates, levels = fetch_measure_levels(stations.measure_id, dt=datetime.timedelta(days=dt))
    

    x = dates
    y = stations

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x, y, 4)

# Convert coefficient into a polynomial that can be evaluated,
# e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

# Plot original data points
    plt.plot(x, y, '.')

# Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))

# Display plot
    plt.show()

plot_water_levels(stations, dates, levels)