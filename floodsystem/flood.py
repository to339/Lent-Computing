from haversine import haversine 
from floodsystem.utils import sorted_by_key
import matplotlib.pyplot as plt
from os import stat
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

#Task 2A - Completed for us

#Task 2B - Chris to complete
def stations_level_over_threshold(stations, tol):
    a = []
    
    for station in stations:
        if station.relative_water_level() is not None and station.relative_water_level() > tol:
            a.append((station.name,station.relative_water_level()))
    return a

    print (stations_level_over_threshold(stations,0.1))
        
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
def flood_warnings(yesterdays_date, todays_date, station_needed, stations, r):
    dates, levels = fetch_measure_levels(
        station_needed.measure_id, dt=datetime.timedelta(days=1))
    yesterdays_ratio = levels[-96]
    day2day_ratio = stations.r - yesterdays_ratio
    #If the ratio is over 1 and rising compared to yesterday's, issue a severe flood warning
    if r > 1:
        if day2day_ratio > 0:
            return "SEVERE FLOOD WARNING"
    #If the ratio is over 1 and decreasing compared to yesterday issue a medium flood warning
        elif day2day_ratio < 0:
            return "Medium Flood Warning"
    #If the ratio is over 1, issue a high flood warning
        else:
            return "High Flood Warning"
    #If the ratio is over 0.5 and the change in ratio is over 1, issue a severe flood warning    
    elif r > 0.5:
    #If the ratio is over 0.5 and the change in ratio is over 0.75 issue a high flood warning
        if day2day_ratio > 0.75:
            return "High Flood Warning"
    #If the ratio is over 0.5 and the change in ratio is over 0.5 issue a medium flood warning
        elif day2day_ratio > 0.5:
            return "Medium Flood Warning"
    #If the ratio is over 0.5 and the change in ratio is between 0 and 0.5 issue a low flood warning
        elif day2day_ratio > 0.5:
            return "Low Flood Warning"
    #Else issue no flood warning
    else:
        return "No Flood Warning"
        
 # Test this by seeing if it issues a flood warning for any occasion that the ratio is less than 1 on a given day - 
 # this should only occur if water levels are receding on a day after a flood warning - 
 # in which case we leave the flood level high for safety reasons.



    
