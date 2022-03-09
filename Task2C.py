from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)

    N = 10
    tol = 0.8
    list = stations_level_over_threshold(stations,tol)
    list.sort(key=lambda x:x[1],reverse=True)
    shortlist = stations_highest_rel_level(list, N)
    print(stations.name, stations.relative_level)

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()