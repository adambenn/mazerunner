from Solvers.AStarSolver import AStarSolver

class BFSSolver(AStarSolver):
    def __init__(self, debug = False):
        super().__init__(lambda x: 0, debug)

    def cost(self, dist, maze, cell):
        return 0