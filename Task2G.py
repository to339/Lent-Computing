from floodsystem.flood import flood_warnings, stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation


stations = build_station_list()


station_name = "Cam"

# Find station
station_needed = None
for station in stations:
    if station.name == station_name:
        station_needed = station
        break

issue_flood_warnings = flood_warnings(station_needed, stations, r)
print (issue_flood_warnings)