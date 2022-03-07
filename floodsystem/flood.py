from haversine import haversine 
from floodsystem.utils import sorted_by_key
import matplotlib.pyplot as plt
from os import stat
import datetime
import numpy
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

#Task 2A - Completed for us

#Task 2B - Chris to complete
def stations_level_over_threshold(stations, tol):
    a = []
    
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            a.append((station,station.relative_water_level()))
    return a

    
        
#Task 2C - Thomas to complete
def stations_highest_rel_level(list, N):
    #order the list of stations given by relative_water_level(self)
    #Print the first N stations from the list
    
    n=0
    at_risk=[]
    while n<N:
        at_risk.append(list[n])
        n+=1
    
    return at_risk

#Task 2D - completed for us

#Task 2E - Thomas to complete
def plot_water_levels(stations, dates, levels, test = False):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(stations.name)
    low, high = stations.typical_range
    plt.axhline(y=high, xmin=0, xmax=5, label = "Normal max")
    plt.axhline(y=low, xmin=0, xmax= 5, label = "Normal min")
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    if not test:
        plt.show()

#Task 2F: Chris to complete

#Task 2G: Thomas to complete

 # Test this by seeing if it issues a flood warning for any occasion that the ratio is less than 1 on a given day - 
 # this should only occur if water levels are receding on a day after a flood warning - 
 # in which case we leave the flood level high for safety reasons.



    
