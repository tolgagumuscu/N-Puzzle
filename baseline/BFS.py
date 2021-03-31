class BFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.queue = list()
        self.counter = 0
        self.visited[root.UID] = root
        self.queue.append(root)

    def run(self, target):
        """ YOUR CODE HERE """
        #control = target.is_equal(self.queue[0])

        while len(self.queue):
            control = self.queue.pop(0)
            self.visited[control.UID] = control
            self.counter += 1

            down = self.graph.reveal_neighbors(control)

            for i in down:
                if i.UID not in self.visited.keys():
                    self.queue.append(i)
            if control.UID == target.UID:
                return True, self .counter, control.step

        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)