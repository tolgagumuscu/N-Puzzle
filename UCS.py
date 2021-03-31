import queue as Q


class UCS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.put((root.step, root, int(root.UID)))

    def run(self, target):
        """ YOUR CODE HERE """
        while not self.queue.empty():
            point = self.queue.get(False,None)[1]
            self.counter += 1
            if point.UID == target.UID:
                return True,self.counter, point.step
            else:
                list_neighbour = self.graph.reveal_neighbors(point)
                for nearby in list_neighbour:
                    if nearby.UID not in self.visited.keys():
                        self.queue.put((nearby.step + target.step, nearby, int(nearby.UID)))
            if point.UID == target.UID:
                return True,self.counter, point.step

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
