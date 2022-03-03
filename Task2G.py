from floodsystem.flood import flood_warnings, stations_level_over_threshold
from floodsystem.stationdata import build_station_list

yesterdays_date = 2/3/2022
todays_date = 3/3/2022
stations = build_station_list()
r = stations_level_over_threshold(stations, tol)

issue_flood_warnings = flood_warnings(yesterdays_date, todays_date, stations, r)
print (issue_flood_warnings)