from datetime import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
from floodsystem.Analysis import polyfit
from plot import plot_water_levels_with_fit
import datetime


stations = build_station_list()

update_water_levels(stations)


#Test 2B
output2B = stations_level_over_threshold(stations,0.8)
check = len(output2B)
assert check != 0

#Test 2C
N = 10
output2C = stations_highest_rel_level(list, N)
check = len(output2C)
assert check == N

#Test 2E
# Build list of stations
stations = build_station_list()
N = 5
level_values = stations_highest_rel_level(stations, N)
# Update latest level data for all stations
update_water_levels(stations)
for stations in level_values:
    dt = 2
    dates, levels = fetch_measure_levels(stations.measure_id, dt=datetime.timedelta(days=dt))
    test = True
    plot_water_levels(stations, dates, levels, test)


assert plot_water_levels(stations, dates, levels, test) == None



#Test 2F
stations = build_station_list()

update_water_levels(stations)

x = stations_level_over_threshold(stations,0.8)
x.sort(key=lambda x:x[1])
top_5 = x[-6:]

dt = 2
for station, value in top_5:
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    if dates:
        test = True
        plot_water_levels_with_fit(station, dates, levels,4, test)

assert plot_water_levels_with_fit(station, dates, levels,4, test) == None



#Test 2G
#This has no inputs, unsure how to test this?
