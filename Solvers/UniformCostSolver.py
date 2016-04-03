from Solvers.solver import *
from Solvers.AStarSolver import *
from Solvers.heuristics import heur_uniform_cost

class UniformCostSolver(Solver):
    def solve(self, maze):
        return AStarSolver(heur_uniform_cost).solve(maze)