from ast import Import
from datetime import datetime
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
from floodsystem.Analysis import polyfit
import datetime
import numpy as np
import matplotlib

stations = build_station_list()

def plot_water_levels(station, dates, levels):

    t = [datetime(2016,12,30), datetime(2016, 12, 31), datetime (2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017,1,4),
     datetime (2017,1,5)]
    level = [0.2,0.7,0.95,0.92,1.02,0.91,0.64]
    

    plt.plot(t,level)

    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45);
    plt.title(station.name)

    plt.tight_layout()

    

    plt.show  


def plot_water_levels_with_fit(station, dates, levels,p, test = False):
    x1 = []
    poly, d0 = polyfit(dates,levels,p)
    
    for i in dates: 
        x1.append(poly(matplotlib.dates.date2num(i)-d0))
    
    low, high = station.typical_range
    plt.axhline(y=high, xmin=0, xmax=5, label = "Normal max", color = "red")
    plt.axhline(y=low, xmin=0, xmax= 5, label = "Normal min", color = "green")
    plt.plot(dates,levels)
    plt.xlabel("dates")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.plot(dates,x1)

    plt.tight_layout()

    
    if test == False:
        plt.show() 