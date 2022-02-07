from unicodedata import name
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

p = [52.2053,0.1218]


stations = (build_station_list(use_cache=True))
data = ((stations_by_distance(stations,p)))



print(data)

