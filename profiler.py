from maze import Maze

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
from Solvers.heuristics import *

import matplotlib.pyplot as plt
from memory_profiler import memory_usage
import os
import copy

GENERATOR_MAZE_SIZE_RANGE = (1, 100)
SOLVER_MAZE_SIZE_RANGE = (1, 50)
MEMORY_INTERVAL = 0.1

def time_func(func, args):
    '''
    :param func: A function to profile
    :param args: Tuple of arguments for func
    :return: The time it takes to run
    '''
    init_time = os.times()[0]
    func(*args)
    return os.times()[0] - init_time

def time_generator(maze, generator):
    '''
    :param maze: A maze object to run the generator on
    :param generator: The generator to time
    :return: Time it takes to generate
    '''
    return time_func(maze.generate, (generator,))

def time_solver(maze, solver):
    '''
    :param maze: A maze object to run the solver on
    :param solver: Solver to time
    :return: Time it takes to solve
    '''
    return time_func(maze.solve, (solver,))

def range_of_mazes(start_size, end_size):
    '''
    Returns generator of mazes of size start_size to end_size
    :param start_size: Start of size range
    :param end_size: End of size range
    :return: Generator of mazes with sizes in [start_size, end_size)
    '''
    for i in range(start_size, end_size):
        yield Maze(i, safe = False)

def time_generator_on_mazes(mazes, generator):
    '''
    Times generator for each maze in mazes
    :param mazes: Iterable of maze objects
    :param generator: The generator to time
    :return: List of times it takes
    '''
    return [time_generator(m, generator) for m in mazes]

def time_solver_on_mazes(mazes, solver):
    '''
    Times solver for each maze in mazes
    :param mazes: Iterable of maze objects
    :param solver: The sovler to time
    :return: List of times it takes
    '''
    return [time_solver(m, solver) for m in mazes]

########################################
############# Memory ###################
def memory_of_func(func, args):
    return max(memory_usage((func , args), interval = MEMORY_INTERVAL))

def memory_of_generator(maze, generator):
    return memory_of_func(maze.generate, (generator,))

def memory_of_solver(maze, solver):
    return memory_of_func(maze.solve, (solver,))

def memory_of_generator_on_mazes(mazes, generator):
    return [memory_of_generator(m, generator) for m in mazes]

def memory_of_solver_on_mazes(mazes, solver):
    return [memory_of_solver(m, solver) for m in mazes]

########################################
############## Costs ###################
def cost_solver_on_mazes(mazes, solver):
    return [len(m.solve(solver)) for m in mazes]

########################################
############## Graphing ################

def graph_generator_times():
    plt.figure(1)
    print("Plotting BFS Generator...")
    l1, = plt.plot(time_generator_on_mazes(
        range_of_mazes(*GENERATOR_MAZE_SIZE_RANGE), BFSGenerator()), label = "Breadth First Search")

    print("Plotting DFS Generator...")
    l2, = plt.plot(time_generator_on_mazes(
        range_of_mazes(*GENERATOR_MAZE_SIZE_RANGE), DFSGenerator()), label = "Depth First Search")

    print("Plotting Kruskals Generator...")
    l3, = plt.plot(time_generator_on_mazes(
        range_of_mazes(*GENERATOR_MAZE_SIZE_RANGE), KruskalsGenerator()), label = "Kruskal's Algorithm")

    print("Plotting Prims Generator...")
    l4, = plt.plot(time_generator_on_mazes(
        range_of_mazes(*GENERATOR_MAZE_SIZE_RANGE), PrimsGenerator()), label = "Prim's Algorithm")

    plt.ylabel("Time (seconds)")
    plt.xlabel("Maze Size")
    plt.legend(handles=[l1, l2, l3, l4], loc=0)
    plt.title("Timing of Generators")
    plt.show()

def graph_solvers(func, title, xlabel, ylabel):
    plts = []
    plt.figure(2)
    print("Generating mazes for solving using DFS Generator...")
    maze_it = range_of_mazes(*SOLVER_MAZE_SIZE_RANGE)
    mazes = []
    d = DFSGenerator()

    i = 1.0
    for m in maze_it:
        m.generate(d)
        mazes.append(m)
        percent = round(i / float(SOLVER_MAZE_SIZE_RANGE[1] - SOLVER_MAZE_SIZE_RANGE[0]), 2) * 100
        if int(percent) % 5 == 0:
            print("{}%".format(percent))
        i += 1

    print("Plotting BFS Solver")
    plts.append(plt.plot(func(mazes, BFSSolver()),
                         label = "Breadth First Search")[0])
    print("Plotting DFS Solver")
    plts.append(plt.plot(func(mazes, DFSSolver()),
                         label = "Depth First Search")[0])
    print("Plotting Uniform Cost Solver")
    plts.append(plt.plot(func(mazes, UniformCostSolver()),
                         label = "Uniform Cost Search")[0])

    print("Euclidean Distance Heuristic")
    print("Plotting Greedy BFS with Euclidean Distance")
    plts.append(plt.plot(func(mazes, GreedyBFSSolver(heur_straight_line)),
                         label = "Greedy BFS Search - Euclidean Distance")[0])
    print("Plotting A* with Euclidean Distance")
    plts.append(plt.plot(func(mazes, AStarSolver(heur_straight_line)),
                         label = "A* Search - Euclidean Distance")[0])
    print("Plotting IDA* with Euclidean Distance")
    plts.append(plt.plot(func(mazes, IDAStarSolver(heur_straight_line)),
                         label = "IDA* Search - Euclidean Distance")[0])

    print("Manhattan Distance Heuristic")
    print("Plotting Greedy BFS with Manhattan Distance")
    plts.append(plt.plot(func(mazes, GreedyBFSSolver(heur_manhattan)),
                         label = "Greedy BFS Search - Manhattan Distance")[0])
    print("Plotting A* with Manhattan Distance")
    plts.append(plt.plot(func(mazes, AStarSolver(heur_manhattan)),
                         label = "A* Search - Manhattan Distance")[0])
    print("Plotting IDA* with Manhattan Distance")
    plts.append(plt.plot(func(mazes, IDAStarSolver(heur_manhattan)),
                         label = "IDA* Search - Manhattan Distance")[0])

    plt.ylabel(xlabel)
    plt.xlabel(ylabel)
    plt.legend(handles=plts, loc=0)
    plt.title(title)
    plt.show()

def graph_solver_times():
    graph_solvers(time_solver_on_mazes, "Timing of Solvers", "Time (seconds)", "Maze Size")

def graph_solver_costs():
    graph_solvers(cost_solver_on_mazes, "Path Costs of Solvers", "# of Nodes", "Maze Size")

def graph_solver_memory():
    graph_solvers(memory_of_solver_on_mazes, "Memory of Solvers", "Memory (MB)", "Maze Size")

if __name__ == "__main__":
    #graph_generator_times()
    #graph_solver_times()
    #graph_solver_costs()
    graph_solver_memory()