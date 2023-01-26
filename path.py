from transport import Transport
from station import Station


class Path:
    def __init__(self):
        self.start_station = None
        self.end_station = None
        self.distance = None
        self.bus_speed = None
        self.taxi_speed = None
        self.bus_names = []
        self.transportsType = [Transport.WALK.name]

    def set_start_station(self, station: Station):
        self.start_station = station

    def set_end_station(self, station: Station):
        self.end_station = station

    def set_distance(self, distance):
        self.distance = distance

    def set_bus_speed(self, speed):
        self.bus_speed = speed

    def set_taxi_speed(self, speed):
        self.taxi_speed = speed

    def set_buses_names(self, names: list):
        self.bus_names = names

    def set_transportsType(self, types: list):
        self.transportsType.extend(types)

    def get_transports_types(self):
        types = self.transportsType
        if (len(self.bus_names) != 0):
            types.append(Transport.BUS.name)
        return types

    def get_money_cost(self, cost):
        return cost * self.distance

    def get_power_cost(self, cost):
        return cost * self.distance

    def get_time_cost(self, speed):
        return self.distance/speed
