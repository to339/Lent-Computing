from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

station = build_station_list()

def test_rivers_with_stations():
    river_names =  rivers_with_stations(station)
    assert(len(river_names)) >1

test_rivers_with_stations()
