
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()

update_water_levels(stations)

def stations_level_over_threshold(stations, tol):
    a = []
    
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            a.append((station.name,station.relative_water_level()))
    return a

print (stations_level_over_threshold(stations,0.1))
        