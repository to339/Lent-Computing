from datetime import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
import datetime
import numpy as np
import matplotlib


# Build list of stations
stations = build_station_list()
N = 5
level_values = stations_highest_rel_level(stations, N)
# Update latest level data for all stations
update_water_levels(stations)



for stations in level_values:
    dt = 2
    dates, levels = fetch_measure_levels(stations.measure_id, dt=datetime.timedelta(days=dt))
    
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    d0 = x[0]
    p_coeff = np.polyfit(x-d0, y, 4)
    
    poly = np.poly1d(p_coeff)
   
    plt.plot(x-d0, y, '.')

    plt.plot(x-d0, poly(x-d0))

    plt.show()

    plot_water_levels(stations, dates, levels)

    return (poly,d0)

print(polyfit(dates, levels, 4))