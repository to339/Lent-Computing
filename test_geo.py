from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.station import *



centre = [52.2053,0.1218]
p = [52.2052,0.128]
station = (build_station_list(use_cache=True))
r=10

def test_rivers_with_stations():
    river_names =  rivers_with_stations(station)
    assert(len(river_names)) >1

def test_stations_by_river():
    stations_on_rivers = stations_by_river(station)
    test_list = stations_on_rivers['River Pinn']
    assert(len(test_list) == 8)

def test_rivers_by_station_number():
    N = 8
    test_length = rivers_by_station_number(station, N)
    assert(len(test_length) == N or len(test_length) > N)



test_rivers_with_stations()

def test_stations_by_distance():
    stations_names =  stations_by_distance(station,p)
    assert(len(stations_names)) >0

test_stations_by_distance()

def test_stations_within_radius():
    stations_within_names =  stations_within_radius(station,centre,r)
    assert(len(stations_within_names)) >0

test_stations_within_radius()

def test_inconsistent_range():
    stations_inconsistent =  inconsistent_typical_range_stations(station)
    assert(len(stations_inconsistent)) >0

test_inconsistent_range()
test_rivers_by_station_number()
test_stations_by_river()
