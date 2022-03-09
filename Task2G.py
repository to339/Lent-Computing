from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
import datetime
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
stations = build_station_list()
update_water_levels(stations)

def run():
    #Collect the ratios for different stations in a town
    #Add the ratios together
    #Average them
    collection = {}
    for station in stations:
        r = station.relative_water_level()
        if r is not None:  
    
            if station.town in collection.keys():
                collection[station.town][0] += r
                collection[station.town][1] += 1

            else:
                collection[station.town]=[r,1]
    

    for key in collection.keys():  
        a = collection[key][0] / collection[key][1]

        if a > 1.25:
            print(key, ": SEVERE FLOOD WARNING")
        elif a > 1:
            print(key, ": High Flood Warning")
        elif a > 0.75:
            print(key, ": Medium Flood Warning")
        elif a > 0.5:
            print(key, ": Low Flood Warning")


if __name__ == "__main__":
    run()