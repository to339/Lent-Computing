from floodsystem.flood import flood_warnings, stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import *
import sympy as sym
from floodsystem.Analysis import polyfit
import datetime
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
stations = build_station_list()
update_water_levels(stations)

for station in stations:
    r = 0
    #dt = 7
    #dates, levels = fetch_measure_levels(
        #station.measure_id, dt=datetime.timedelta(days=dt))

    #Attempt at gradient of graph from 2E it failed very very badly
    #d = polyfit(dates,levels,4)
    #x = matplotlib.dates.date2num(dates)
    #q = d[0].deriv()
    #vale = q(x[len(x)-1])
    #print(q)
    #print(vale)
    #day2day_ratio = q
    try:
        if station.relative_water_level():
            r = station.relative_water_level()
        if r > 1.25:
            print(station.name, ": SEVERE FLOOD WARNING")
        elif r > 1:
            print(station.name, ": High Flood Warning")
        elif r > 0.75:
            print(station.name, ": Medium Flood Warning")
        elif r > 0.5:
            print(station.name, ": Low Flood Warning")
    except:
        print()