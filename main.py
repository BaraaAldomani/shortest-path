
from input import Data
from node import Node
from person import Person
from structure import Structure
from logic import Logic


def main():
    data = Data()
    data.init()

    node = Node(data.start_station, data.final_station, data.person)
    s = Structure(node, data)

    logic = Logic(s)
    logic.AStar()
    # logic.BFS()


main()
