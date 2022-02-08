from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)



stations = (build_station_list(use_cache=True))




print ((inconsistent_typical_range_stations(stations)))

