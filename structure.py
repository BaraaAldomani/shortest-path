import sys
import copy
from node import Node
from input import Data
from path import Path
from next_move import NextMove
from transport import Transport
import numpy as nb
import time
from person import Person
from datetime import timedelta


class Structure:
    visited: list[Node] = []
    track = []

    def __init__(self, node: Node, data: Data) -> None:
        self.node = node
        self.stations = data.stations
        self.paths = data.paths
        self.data = data
        pass

    def check_move(self, node: Node):
        enabled_paths = []

        path: Path
        for path in self.paths:
            time = 0
            if node.current_station.name == path.start_station.name:
                for type in path.get_transports_types():
                    if type == 'WALK':
                        money = path.get_money_cost(self.data.walk_money_cost)
                        power = path.get_power_cost(self.data.walk_power_cost)
                        time = path.get_time_cost(self.data.walk_speed)
                        if node.person.power > power:
                            enabled_paths.append(
                                NextMove(path, node, [type, 'walk'], money, power, time, False))
                    elif type == 'BUS':
                        money = self.data.bus_money_cost
                        power = path.get_power_cost(self.data.bus_power_cost)
                        time = path.get_time_cost(path.bus_speed)
                        if node.person.power > power:
                            if node.person.money > money:
                                enabled_paths.append(
                                    NextMove(path, node, [type, path.bus_names[0]], money, power, time, True))
                    elif type == 'TAXI':
                        money = path.get_money_cost(self.data.taxi_money_cost)
                        power = path.get_power_cost(self.data.taxi_power_cost)
                        time = path.get_time_cost(path.taxi_speed)
                        if node.person.power > power:
                            if node.person.money > money:
                                enabled_paths.append(
                                    NextMove(path, node, [type, 'taxi'], money, power, time, True))
        return enabled_paths

    def move(self, next: NextMove):
        current_station = next.path.end_station

        # time editing and cost
        time = 0
        money = 0
        # the person rides the transports
        if next.node.person.is_passenger:
            # person came with a bus
            if next.node.transport[0] == Transport.BUS.name:
                # bus -> bus
                if next.transport[0] == Transport.BUS.name:
                    # bus -> the same bus
                    if next.node.transport[1] == next.transport[1]:
                        money = 0
                        time = next.node.time + next.time_cost
                    else:
                        money = next.money_cost
                        time = next.node.time + next.time_cost + next.node.current_station.bus_wait
                # bus -> taxi
                elif next.transport[0] == Transport.TAXI.name:
                    money = next.money_cost
                    time = next.node.time + next.time_cost + next.node.current_station.taxi_wait
                # bus -> walk
                elif next.transport[0] == Transport.WALK.name:
                    money = next.money_cost
                    time = next.node.time + next.time_cost
            # person came with a taxi
            elif next.node.transport[0] == Transport.TAXI.name:
                # taxi -> bus
                if next.transport[0] == Transport.BUS.name:
                    money = next.money_cost
                    time = next.node.time + next.time_cost + next.node.current_station.bus_wait
                # taxi -> taxi
                elif next.transport[0] == Transport.TAXI.name:
                    money = next.money_cost
                    time = next.node.time + next.time_cost
                # taxi -> walk
                elif next.transport[0] == Transport.WALK.name:
                    money = next.money_cost
                    time = next.node.time + next.time_cost
        # the person doesn't ride the transports
        else:
            # walk -> bus
            if next.transport[0] == Transport.BUS.name:
                money = next.money_cost
                time = next.node.time + next.time_cost + next.node.current_station.bus_wait
            # walk -> taxi
            elif next.transport[0] == Transport.TAXI.name:
                money = next.money_cost
                time = next.node.time + \
                    next.path.get_time_cost(
                        next.path.taxi_speed) + next.node.current_station.taxi_wait
            # walk -> walk
            elif next.transport[0] == Transport.WALK.name:
                money = next.money_cost
                time = next.node.time + next.time_cost

        if next.transport[0] == Transport.TAXI.name:
            power = next.node.person.power + next.power_cost
        else:
            power = next.node.person.power - next.power_cost
        person = Person()
        person.set_money(next.node.person.money - money)
        person.set_power(power)
        person.set_is_passenger(next.is_passenger)

        # cost = self.time_heuristic(money)
        cost = self.time_heuristic(time)
        # cost = self.time_heuristic(power)
        # cost = self.all_heuristic(money, power)

        return Node(current_station, next.node.goal_station, person,  next.transport, time, next.node, cost)

    def get_next_states(self, node: Node):
        next_states: list[Node] = []
        temp_node = copy.deepcopy(node)
        states = self.check_move(temp_node)
        for state in states:
            next = self.move(state)
            next_states.append(next)

        return next_states

    def time_heuristic(self, time):
        return time

    def power_heuristic(self, power):
        return power

    def money_heuristic(self, money):
        return money

    def all_heuristic(self, money, power):
        return money - power

    def equal(self, node: Node, temp_node: Node):
        return node == temp_node

    def check_if_in_visited(self, node: Node):
        for state in self.visited:
            if (self.equal(state, node)):
                return True
        return False

    def is_final_state(self, node: Node):
        if node.goal_station.name == node.current_station.name:

            return True
        return False

    def get_track(self, state: Node):
        temp = copy.deepcopy(state)
        while True:
            if (temp.father == None):
                self.track.append(temp)
                break
            elif (temp.father != None):
                self.track.append(temp)
                temp = temp.father

    def time_in_hour(self, min):
        return str(timedelta(minutes=min))[:-3]

    def time_in_second(self, sec):
        return str(timedelta(seconds=sec))[:-3]

    def print_soluation(self, start):
        end = time.time()
        temp = self.track[::-1]
        for i in range(len(temp)):
            print('='*50)
            print(f'Node : {temp[i].current_station.name}')
            print(
                f'Time : {self.time_in_hour(temp[i].time*60)}')
            print(f'Money: {temp[i].person.money}')
            print(f'power: {temp[i].person.power}')
            print(f'Transport : {temp[i].transport}')
            print('='*50)
            print()
        print('='*50)
        print(f'Time Excution : {self.time_in_second(end - start)}')
        print(f'Visited node : {len(self.visited)}')
        print(f'Track node : {len(self.track)}')
        print('='*50)
