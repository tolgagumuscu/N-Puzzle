import queue as Q


class AStar:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.visited = dict()
        self.queue = Q.PriorityQueue()
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        # I would create counter as 0 but we already assigned at the top
        self.queue.put((self.manhattan_distance(self.root, target),self.root,int(self.root.UID)))
        already_been = {}
        in_line = Q.PriorityQueue()
        in_line.put((1,self.root))
        already_been[self.root.UID] = self.root

        while not self.queue.empty():
            self.counter +=1
            last_one = self.queue.get(False, None)[1]

            check = bool(last_one.UID == target.UID)

            if (check):
                return True, self.counter, last_one.step

            close = self.graph.reveal_neighbors(last_one)

            for i in range(len(close)):
                if close[i].UID not in already_been:
                    length = self.manhattan_distance(close[i],target)
                    self.queue.put((length, close[i], int(close[i].UID)))

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0

    def manhattan_distance(self, node, end):
        arr = [0] * (self.graph.size + 1)
        brr = [0] * (self.graph.size + 1)
        for i in range(len(node.g_node)):
            for j in range(len(node.g_node[i])):
                arr[node.g_node[i][j]] = [i, j]

        for i in range(len(end.g_node)):
            for j in range(len(end.g_node[i])):
                brr[end.g_node[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0] - brr[i][0]) + abs(arr[i][1] - brr[i][1])
        return dist
