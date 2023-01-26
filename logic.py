
from structure import Structure
import queue as Queue
import time


class Logic:
    def __init__(self, structure: Structure) -> None:
        self.structure = structure

    def BFS(self):
        now = time.time()
        queue = Queue.Queue()
        queue.put(self.structure.node)
        self.structure.visited.append(self.structure.node)
        while queue:
            temp = queue.get()
            if self.structure.is_final_state(temp):
                self.structure.get_track(temp)
                break
            for state in self.structure.get_next_states(temp):
                if (not self.structure.check_if_in_visited(state)):
                    queue.put(state)
                    self.structure.visited.append(state)
        self.structure.print_soluation(now)

    def AStar(self):
        now = time.time()
        queue = Queue.PriorityQueue()
        queue.put(self.structure.node)
        self.structure.visited.append(self.structure.node)
        while queue.queue:
            temp_node = queue.queue.pop(0)
            if self.structure.is_final_state(temp_node):
                self.structure.get_track(temp_node)
                break
            for state in self.structure.get_next_states(temp_node):
                if (not self.structure.check_if_in_visited(state)):
                    queue.put(state)
                    self.structure.visited.append(state)

        self.structure.print_soluation(now)
