class Solver:
    def __init__(self, debug = False):
        self.debug = debug

    def isGoal(self, maze, cell):
        return maze.exit is cell

    def solve(self, maze):
        return []

class HeuristicSolver(Solver):
    def __init__(self, heuristic, debug = False):
        super().__init__(debug)
        self.heuristic = heuristic

    def cost(self, dist, maze, cell):
        return dist + 1 + self.heuristic(maze, cell)
