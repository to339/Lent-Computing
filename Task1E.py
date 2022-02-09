from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number, rivers_with_stations, stations_by_river
from floodsystem.utils import sorted_by_key

def run():
    stations = build_station_list(use_cache=True)
    N = 9
    river_names = rivers_by_station_number(stations, N)
    
    print(river_names)
    

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()