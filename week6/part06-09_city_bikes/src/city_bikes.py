# Write your solution here
import math

def get_station_data(filename: str):
    station_names = {}
    with open(filename) as station_file:
        for line in station_file:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            station_names[parts[3]] = (float(parts[0]), float(parts[1]))

    return station_names

def distance(stations: dict, station1: str, station2: str):
    longitude_1 = 0
    longitude_2 = 0
    latitude_1 = 0
    latitude_2 = 0
    for key,value in stations.items():
        if key == station1:
            longitude_1 = value[0]
            latitude_1 = value[1]
        if key == station2:
            longitude_2 = value[0]
            latitude_2 = value[1]
    x_km = (longitude_1 - longitude_2) * 55.26
    y_km = (latitude_1 - latitude_2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2) #Pythagorean theorem

    return distance_km

def greatest_distance(stations: dict):
    longitude_1 = 0
    longitude_2 = 0
    latitude_1 = 0
    latitude_2 = 0
    station1 = ""
    station2 = ""
    greatest_km = 0
    for key1 in stations: #stations[key][0,1] for values (long. / lat.)
        longitude_1 = stations[key1][0]
        latitude_1 = stations[key1][1]
        for key2, value in stations.items():
            longitude_2 = value[0]
            latitude_2 = value[1]

            x_km = (longitude_1 - longitude_2) * 55.26
            y_km = (latitude_1 - latitude_2) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)

            if distance_km > greatest_km:
                station1 = key1
                station2 = key2
                greatest_km = distance_km

    return (station1, station2, greatest_km)

if __name__ == "__main__":
    #print(get_station_data("stations1.csv"))

    example_stations = get_station_data('stations1.csv')
    d = distance(example_stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(example_stations, "Viiskulma", "Kaivopuisto")
    print(d)

    
    example_stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(example_stations)
    print(station1, station2, greatest)