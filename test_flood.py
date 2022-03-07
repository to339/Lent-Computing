from floodsystem.flood import *

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()

update_water_levels(stations)


#Test 2B

output2B = stations_level_over_threshold(stations,0.8)
check = len(output2B)
if check != 0:
    print("2B Length Check: Pass")
else:
    print("2BLength Check: Fail")


#Test 2C
N = 10
output2C = stations_highest_rel_level(list, N)
check = len(output2C)
if check == N:
    print("2C Length Check: Pass")
else:
    print("2C Length Check: Fail")

#Test 2E
from datetime import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
import datetime

# Build list of stations
stations = build_station_list()
N = 5
level_values = stations_highest_rel_level(stations, N)
# Update latest level data for all stations
update_water_levels(stations)
for stations in level_values:
    dt = 2
    dates, levels = fetch_measure_levels(stations.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(stations, dates, levels)


assert plot_water_levels(stations, dates, levels) == None
print ("2E Output Check: Pass")

from datetime import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
from floodsystem.Analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
import datetime

from plot import plot_water_levels_with_fit


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
        
        plot_water_levels_with_fit(station, dates, levels,4)

assert plot_water_levels_with_fit(station, dates, levels,4) == None
print ("2F Output Check: Pass")



#Test 2G
#This has no inputs, unsure how to test this as well?
