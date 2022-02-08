from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

stations = build_station_list()

def test_rivers_with_stations():
    river_names =  rivers_with_stations(stations)
    assert(len(river_names)) >1

def test_stations_by_river():
    stations_on_rivers = stations_by_river(stations)
    test_list = stations_on_rivers['River Pinn']
    assert(len(test_list) == 8)

def test_rivers_by_station_number():
    N = 8
    test_length = rivers_by_station_number(stations, N)
    assert(len(test_length) == N or len(test_length) > N)



test_rivers_with_stations()
test_rivers_by_station_number()
test_stations_by_river()