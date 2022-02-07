# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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

    


    
def rivers_by_station_number(stations, N):
    #A function which provides the N rivers with the most stations
    stations_on_river = {}
    for station in stations:
        key = station.river
        if key in stations_on_river.keys():
            stations_on_river[key] += 1
        else:
            stations_on_river[key] = 1
    number_list = sorted(stations_on_river.items(), key=lambda x: x[1], reverse=True)
    
    final_list = number_list[:N]
    a = N
    check = True
    while check:
        if number_list[a-1][1] == number_list[a][1]:
            final_list.append(number_list[a])
            a = a+1
        else:
            check = False
    
    
    return final_list



