from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

stations = build_station_list()
N = 10
list = stations_level_over_threshold(stations,100)
list.sort(key=lambda x:x[1])
shortlist = stations_highest_rel_level(list, N)
print(shortlist)