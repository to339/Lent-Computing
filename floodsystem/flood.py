from haversine import haversine 
from .utils import sorted_by_key
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

#Task 2A - Completed for us

#Task 2B - Chris to complete

#Task 2C - Thomas to complete
def stations_highest_rel_level(stations, N):
    #order the list of stations given by relative_water_level(self)
    #Print the first N stations from the list
    ordered_stations = stations[N].sort()
    
    n=0
    at_risk=()
    while n<N:
        at_risk.append(ordered_stations[0,n])
        n+=1
    
    return at_risk
#Task 2D - completed for us

#Task 2E - Thomas to complete
def plot_water_levels(stations, dates, levels):
    
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(stations.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

#Task 2F: Chris to complete

#Task 2G: Thomas to complete
    #If the ratio is over 1, issue a high flood warning
    #If the ratio is over 1 and rising compared to yesterday's, issue a severe flood warning
    #If the change in ratio is over 1, issue a severe flood warning
    #If the change in ratio is over 0.75 issue a high flood warning
    #If the ratio is over 0.5 and the change in ratio is over 0.5 issue a low flood warning
    