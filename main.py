from Generators.DFSGenerator import *
from Generators.KruskalsGenerator import *
from Solvers.DFSSolver import *
from Solvers.UniformCostSolver import *
from Solvers.AStarSolver import *
from Solvers.GreedyBFSSolver import *
from Solvers.BFSSolver import *
import graphics
from maze import *
from Solvers.heuristics import *

if __name__ == "__main__":
    random.seed(1456345)
    maze = Maze(15)
    print("Testing DFS generation")

    # maze.generate(DFSGenerator(debug = True))
    # maze.generate(DFSGenerator())
    maze.generate(KruskalsGenerator())
    #print(maze.graphicalRepresentation())

    #path = maze.solve(UniformCostSolver())
    path = maze.solve(AStarSolver(heur_straight_line))
    #path = maze.solve(DFSSolver())
    #path = maze.solve(GreedyBFSSolver(heur_straight_line))
    #path = maze.solve(BFSSolver())

    g = graphics.MazeGraphics(maze)
    g.run(path)