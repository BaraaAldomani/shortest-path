from person import Person
from station import Station


class Node:
    def __init__(self, current_station: Station, final_station: Station, person: Person, transport=['WALK', 'walk'], time=0, father=None, cost=0):
        self.father = father
        self.current_station = current_station
        self.goal_station = final_station
        self.person = person
        self.time = time
        self.transport = transport
        self.cost = cost

    def __eq__(self, node: object) -> bool:
        if isinstance(node, Node):
            a = self.current_station == node.current_station
            b = self.goal_station == node.goal_station
            c = self.person == node.person
            d = self.time == node.time
            e = self.transport == node.transport
            f = self.father == node.father
            return a and b and c and d and e and f

    def __lt__(self, other):
        # if (self.h == other.h):
        #     return self.cost < other.cost
        return self.cost < other.cost
