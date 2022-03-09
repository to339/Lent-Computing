from datetime import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import *
from floodsystem.Analysis import polyfit
from floodsystem.flood import stations_level_over_threshold
import datetime

from plot import plot_water_levels_with_fit


stations = build_station_list()

update_water_levels(stations)
x = stations_level_over_threshold(stations,0.8)
x.sort(key=lambda x:x[1])
top_5 = x[-6:]
# print(top_5)

    
def run():
    stations = build_station_list()
    N = 5
    level_values = stations_highest_rel_level(stations, N)
    # Update latest level data for all stations
    update_water_levels(stations)
    dt = 2
    
    for station, value in top_5:
        print(station.name, value)
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        if dates:
            
            plot_water_levels_with_fit(station, dates, levels,4)
    plot_water_levels(station, dates, levels)

run()