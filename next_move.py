from path import Path
from node import Node


class NextMove:
    def __init__(self, path: Path, node: Node, transport: list, money_cost, power_cost, time_cost, is_passenger) -> None:
        self.path = path
        self.node = node
        self.transport = transport
        self.money_cost = money_cost
        self.power_cost = power_cost
        self.time_cost = time_cost
        self.is_passenger = is_passenger
