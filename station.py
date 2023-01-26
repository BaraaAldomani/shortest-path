

class Station:
    def __init__(self):
        self.name = None
        self.bus_wait = None
        self.taxi_wait = None

    def __eq__(self, station: object) -> bool:
        if isinstance(station, Station):
            a = self.name == station.name
            b = self.bus_wait == station.bus_wait
            c = self.taxi_wait == station.taxi_wait
            return (a and b and c)

    def set_name(self, name):
        self.name = name

    def set_bus_wait(self, wait):
        self.bus_wait = wait

    def set_taxi_wait(self, wait):
        self.taxi_wait = wait
