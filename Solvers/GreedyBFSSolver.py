from Solvers.AStarSolver import AStarSolver

class GreedyBFSSolver(AStarSolver):
    def cost(self, dist, maze, cell):
        return self.heuristic(maze, cell)