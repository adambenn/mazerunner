class Solver:
    UPDATE_DELAY = 0
    def __init__(self, debug = False, graphics = None):
        self.debug = debug
        self.graphics = graphics

    def isGoal(self, maze, cell):
        return maze.exit is cell

    def solve(self, maze):
        return []

class HeuristicSolver(Solver):
    def __init__(self, heuristic, debug = False, graphics = None):
        super().__init__(debug, graphics)
        self.heuristic = heuristic

    def cost(self, dist, maze, cell):
        return float(dist) + 1.0 + self.heuristic(maze, cell)
