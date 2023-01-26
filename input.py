from station import Station
from path import Path
from transport import Transport as t
from person import Person


class Data:
    stations = []
    start_station = Station()
    final_station = Station()
    paths = []
    busesNames = []

    bus_money_cost = 400
    bus_power_cost = 5
    taxi_money_cost = 1000
    taxi_power_cost = 5
    walk_money_cost = 0
    walk_power_cost = 10
    walk_speed = 5.5
    person = Person()

    def init(self):
        self.init_stations()
        self.init_buses_Names()
        self.init_paths()
        self.init_person()

    def init_stations(self):
        s = Station()
        s.set_name('A')
        s.set_bus_wait(10/60)
        s.set_taxi_wait(5/60)
        self.stations.append(s)

        s = Station()
        s.set_name('B')
        s.set_bus_wait(8/60)
        s.set_taxi_wait(5/60)
        self.stations.append(s)

        s = Station()
        s.set_name('C')
        s.set_bus_wait(6/60)
        s.set_taxi_wait(3/60)
        self.stations.append(s)

        s = Station()
        s.set_name('D')
        s.set_bus_wait(5/60)
        s.set_taxi_wait(2/60)
        self.stations.append(s)

        s = Station()
        s.set_name('E')
        s.set_bus_wait(7/60)
        s.set_taxi_wait(5/60)
        self.stations.append(s)

        s = Station()
        s.set_name('F')
        s.set_bus_wait(3/60)
        s.set_taxi_wait(3/60)
        self.stations.append(s)

        s = Station()
        s.set_name('G')
        s.set_bus_wait(4/60)
        self.stations.append(s)

        s = Station()
        s.set_name('H')
        s.set_bus_wait(9/60)
        s.set_taxi_wait(3/60)
        self.stations.append(s)

        self.start_station = self.stations[0]
        self.final_station = self.stations[-1]

    def init_buses_Names(self):
        self.busesNames.append('AC')
        self.busesNames.append('BC')
        self.busesNames.append('CE')
        self.busesNames.append('DE')
        self.busesNames.append('GE')
        self.busesNames.append('GF')
        self.busesNames.append('FH')

    def init_paths(self):
        p = Path()
        p.set_start_station(self.stations[0])
        p.set_end_station(self.stations[1])
        p.set_distance(2)
        p.set_taxi_speed(60)
        p.set_transportsType([t.TAXI.name])
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[1])
        p.set_end_station(self.stations[2])
        p.set_buses_names([self.busesNames[1]])
        p.set_distance(3.6)
        p.set_bus_speed(50)
        p.set_taxi_speed(60)
        p.set_transportsType([t.TAXI.name])
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[1])
        p.set_end_station(self.stations[3])
        p.set_distance(5.2)
        p.set_taxi_speed(60)
        p.set_transportsType([t.TAXI.name])
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[0])
        p.set_end_station(self.stations[2])
        p.set_buses_names([self.busesNames[0]])
        p.set_distance(3)
        p.set_bus_speed(50)
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[2])
        p.set_end_station(self.stations[4])
        p.set_buses_names([self.busesNames[0], self.busesNames[2]])
        p.set_distance(0.9)
        p.set_bus_speed(50)
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[3])
        p.set_end_station(self.stations[4])
        p.set_buses_names([self.busesNames[3]])
        p.set_distance(4)
        p.set_bus_speed(50)
        p.set_taxi_speed(60)
        p.set_transportsType([t.TAXI.name])
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[3])
        p.set_end_station(self.stations[6])
        p.set_distance(0.5)
        p.set_bus_speed(50)
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[6])
        p.set_end_station(self.stations[5])
        p.set_buses_names([self.busesNames[5]])
        p.set_distance(1.5)
        p.set_bus_speed(50)
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[6])
        p.set_end_station(self.stations[4])
        p.set_buses_names([self.busesNames[4]])
        p.set_distance(1.2)
        p.set_bus_speed(50)
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[5])
        p.set_end_station(self.stations[7])
        p.set_buses_names([self.busesNames[6]])
        p.set_distance(4)
        p.set_bus_speed(50)
        p.set_taxi_speed(60)
        p.set_transportsType([t.TAXI.name])
        self.paths.append(p)

        p = Path()
        p.set_start_station(self.stations[4])
        p.set_end_station(self.stations[7])
        p.set_distance(9)
        p.set_taxi_speed(60)
        p.set_transportsType([t.TAXI.name])
        self.paths.append(p)

    def init_person(self):
        self.person.set_money(10000)
        self.person.set_power(100)
