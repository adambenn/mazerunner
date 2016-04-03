class Solver:
    def __init__(self, debug = False):
        self.debug = debug

    def isGoal(self, maze, cell):
        return maze.exit is cell

    def solve(self, maze):
        return []