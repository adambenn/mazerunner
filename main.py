from Generators.DFSGenerator import *
from Solvers.DFSSolver import *
import graphics
from maze import *

if __name__ == "__main__":
    #random.seed(12345)
    maze = Maze(15)
    print("Testing DFS generation")

    # maze.generate(DFSGenerator(debug = True))
    maze.generate(DFSGenerator())
    #print(maze.graphicalRepresentation())

    path = maze.solve(DFSSolver())
    g = graphics.MazeGraphics(maze)
    g.run(path)