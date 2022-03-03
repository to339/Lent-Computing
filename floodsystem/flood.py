from haversine import haversine 
from .utils import sorted_by_key
import matplotlib

#Task 2A - Completed for us

#Task 2B - Chris to complete

#Task 2C - Thomas to complete
def stations_highest_rel_level(stations, N):
    #order the list of stations given by relative_water_level(self)
    #Print the first N stations from the list
    ordered_stations = stations.sort()
    
    n=0
    at_risk=()
    while n<N:
        at_risk.append(ordered_stations[0,n])
        n+=1
    
    return at_risk
#Task 2D - completed for us

#Task 2E - Thomas to complete
def plot_water_levels(station, dates, levels):
    pass

#Task 2F: Chris to complete

#Task 2G: Thomas to complete

def random_sentence_to_remove_error():
    pass