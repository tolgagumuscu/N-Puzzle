class DFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.visited = dict()
        self.stack = list()
        self.stack.append(root)
        self.counter = 0

    def run(self, target):
        """ YOUR CODE HERE """
        boardVisited = set()
        global control
        while len(self.stack):
            control = self.stack.pop(-1)
            self.visited[control.UID] = control
            boardVisited.add(control.UID)
            self.counter += 1

            if control.UID == target.UID:
                return True, self.counter, control.step

            possiblePaths = reversed(self.graph.reveal_neighbors(control))

            for path in possiblePaths:
                if path.UID not in self.visited.keys():
                    nearby = [path]
                    self.stack.append(path)
                    self.stack.extend(nearby)
                    boardVisited.add(path.UID)
        # return 3 items
        # a: bool (match found or not)
        # b: int (counter)
        # c: int (depth)
        return False, 0, 0
