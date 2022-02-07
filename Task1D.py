
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations, stations_by_river
def run():
    stations = build_station_list(use_cache=True)
    river_names = rivers_with_stations(stations)
    print(river_names[:10])
    print()

    stations_on_rivers = stations_by_river(stations)
    stations_list1 = stations_on_rivers['River Cam']
    stations_list1.sort()
    print(stations_list1)
    print()

    stations_list2 = stations_on_rivers['Spen Beck']
    stations_list2.sort()
    print(stations_list2)
    print()
    
    stations_list3 = stations_on_rivers['River Thames']
    stations_list3.sort()
    print(stations_list3)
    print()

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
