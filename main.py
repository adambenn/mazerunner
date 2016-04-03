from Generators.DFSGenerator import *
from Solvers.DFSSolver import *
from maze import *

if __name__ == "__main__":
    #random.seed(12345)
    maze = Maze(5)
    print("Testing DFS generation")

    # maze.generate(DFSGenerator(debug = True))
    maze.generate(DFSGenerator())
    print(maze.graphicalRepresentation())

    path = maze.solve(DFSSolver())
    print("Solution path:")
    for p in path:
        print(p)