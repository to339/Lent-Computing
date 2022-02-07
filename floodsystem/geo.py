# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine 
from .utils import sorted_by_key  # noqa




def rivers_with_stations(stations):
    #List of all rivers with a monitoring station
    river_name = []
    for station in stations:
        if station.river not in river_name:
            river_name.append(station.river)
    
    river_name.sort()
    return river_name
    
def stations_by_river(stations):
    #Selecting one river in the list results in the printing of all stations on that river
    stations_on_river = {}
    for station in stations:
        key = station.river
        if key in stations_on_river.keys():
            stations_on_river[key].append(station.name)
        else:
            stations_on_river[key] = [station.name]
    return stations_on_river

def stations_by_distance(stations,p):
    stations_name = []
    distance = []
    
    for station in stations:
        stations_name.append([station.river,station.town])
        Data = haversine(p,station.coord)
        distance.append(Data)
        lst_tuple = list(zip(stations_name,distance))
        sorted_by_second = sorted(lst_tuple, key=lambda tup: tup[1])
        
        Answer = [sorted_by_second[:10]]
        Answer.append(sorted_by_second[-10:])

        
    return(Answer)
    


    
def rivers_by_station_number(stations):
    #A function which provides the N rivers with the most stations
    pass



