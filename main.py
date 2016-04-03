from Generators.DFSGenerator import *
from Solvers.DFSSolver import *
from Solvers.UniformCostSolver import *
import graphics
from maze import *

if __name__ == "__main__":
    #random.seed(14345)
    maze = Maze(15)
    print("Testing DFS generation")

    # maze.generate(DFSGenerator(debug = True))
    maze.generate(DFSGenerator())
    #print(maze.graphicalRepresentation())

    path = maze.solve(UniformCostSolver())
    #path = maze.solve(DFSSolver())
    g = graphics.MazeGraphics(maze)
    g.run(path)