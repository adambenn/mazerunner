from Generators.DFSGenerator import *
from Generators.KruskalsGenerator import *
from Generators.BFSGenerator import *
from Generators.PrimsGenerator import *
from Solvers.DFSSolver import *
from Solvers.UniformCostSolver import *
from Solvers.AStarSolver import *
from Solvers.GreedyBFSSolver import *
from Solvers.BFSSolver import *
from Solvers.IDAStarSolver import *
import graphics
import os
from maze import *
from Solvers.heuristics import *

def getYesNo(string):
    while True:
        var = input(string)
        if var == 'yes' or var == 'no':
            return var == 'yes'

def getInt(string, validIntRange=0):
    validIntRange = [i for i in range(validIntRange)]
    while True:
        try:
            n = int(input(string))
        except:
            continue
        if validIntRange == [] or n in validIntRange:
            return n

if __name__ == "__main__":

    debug = False
    #random.seed(14345)

    exit = False

    while not exit:
        print()

        size = getInt("Set maze size: ")
        print("Creating a {0}x{0} maze.".format(size))
        maze = Maze(size)

        print("Select a maze generating algorithm:")
        Generator = getInt("0: BFS, 1: DFS, 2: Kruskal's, 3: Prim's -- ", 4)
        generator_simulator = graphics.MazeGraphics if getYesNo("Simulate maze generation? (yes/no) ") else None

        if Generator == 0:
            Generator = BFSGenerator
            genName = 'Breadth-First Search'
        elif Generator == 1:
            Generator = DFSGenerator
            genName = 'Depth-First Search'
        elif Generator == 2:
            Generator = KruskalsGenerator
            genName = "Kruskal's Algorithm"
        elif Generator == 3:
            Generator = PrimsGenerator
            genName = "Prim's Algorithm"

        print("----------------------------")
        print('Using {} to Generate the Maze'.format(genName))

        init_time = os.times()[0]
        maze.generate(Generator(debug, generator_simulator))
        timetime = os.times()[0] - init_time

        print('Generator time: {}'.format(time))
        print("----------------------------")

        print("Select a maze solving algorithm:")
        solverID = getInt("0: BFS, 1: DFS, 2: UniformCost, 3: GreedyBFS, 4: A*, 5: IDA* -- ", 6)

        if solverID == 0:
            Solver = BFSSolver
            strategy = 'Breadth-First Search'
        elif solverID == 1:
            Solver = DFSSolver
            strategy = 'Depth-First Search'
        elif solverID == 2:
            Solver = UniformCostSolver
            strategy = 'Uniform-Cost Search'
        else:
            if solverID == 3:
                Solver = GreedyBFSSolver
                strategy = 'Greedy Best-First Search'
            elif solverID == 4:
                Solver = AStarSolver
                strategy = 'A* Search'
            else:
                Solver = IDAStarSolver
                strategy = "IDA* Search"

            print("Select a heuristic:")
            heur = getInt("0: Straight Line, 1: Manhattan Distance -- ", 2)
            if heur == 0:
                heur = "Straight Line"
                heuristic = heur_straight_line
            else:
                heur = "Manhattan Distance"
                heuristic = heur_manhattan
            strategy = "{} with {} heuristic".format(strategy, heur)

        solver_simulator = graphics.MazeGraphics if getYesNo("Simulate maze solver? (yes/no) ") else None

        print("----------------------------")
        print('Search Strategy: {}'.format(strategy))

        if solverID > 2:
            init_time = os.times()[0]
            path = maze.solve(Solver(heuristic = heuristic, graphics = solver_simulator))
            time = os.times()[0] - init_time
        else:
            init_time = os.times()[0]
            path = maze.solve(Solver(graphics = solver_simulator))
            time = os.times()[0] - init_time

        print('Search time: {}'.format(time))
        print('Solution cost: {}'.format(len(path)))
        print("----------------------------")

        if getYesNo("Show solution? (yes/no) "):
            print("Close all graphics windows to continue.")
            g = graphics.MazeGraphics(maze)
            g.run(path)
            g.top.mainloop()

        exit = getYesNo("Exit? (yes/no) ")
