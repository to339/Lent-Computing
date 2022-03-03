
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()

update_water_levels(stations)



list = stations_level_over_threshold(stations,3)
list.sort(key=lambda x:x[1])
print(list)