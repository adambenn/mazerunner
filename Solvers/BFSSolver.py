from Solvers.AStarSolver import AStarSolver

class BFSSolver(AStarSolver):
    def __init__(self, debug = False, graphics = None):
        super().__init__(lambda x: 0, debug, graphics)

    def cost(self, dist, maze, cell):
        return 0