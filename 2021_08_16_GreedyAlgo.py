# Set Covering Problem 集合覆盖问题
# 有若干电台，每个电台可以覆盖若干地区，找出用最少的电台覆盖最多地区的解决方案

states_ToBe_Covered = {  # Set Literal
                        "mt", "wa", "or", "id",
                        "nv", "ut", "ca", "az"
                      }

station_covering_mapping = {}  # dict Literal

station_covering_mapping["Station One"] = {"id", "nv", "ut"}
station_covering_mapping["Station Two"] = {"wa", "id", "mt"}
station_covering_mapping["Station Three"] = {"or", "nv", "ca"}
station_covering_mapping["Station Four"] = {"nv", "ut"}
station_covering_mapping["Station Five"] = {"ca", "az"}

solution_of_stations = []

while states_ToBe_Covered:
    best_station = None
    states_covered_sofar = set()
    # find the most covered station
    for station, states in station_covering_mapping.items():
        covered_states_for_thisStation = states & states_ToBe_Covered
        if len(covered_states_for_thisStation) > len(states_covered_sofar):
            best_station = station
            states_covered_sofar = covered_states_for_thisStation
    solution_of_stations.append(best_station)
    states_ToBe_Covered -= states_covered_sofar

print(solution_of_stations)
