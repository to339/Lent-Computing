from unicodedata import name
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


centre = [52.2053,0.1218]
stations = (build_station_list(use_cache=True))
r=10

print (stations_within_radius(stations, centre, r))