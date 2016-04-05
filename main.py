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

if __name__ == "__main__":

    '''
    Configure everything here
    '''
    random.seed(14345)
    maze = Maze(15)
    debug = False
    showGraphics = True
    simulate_generation = True
    simulate_solver = True
    heuristic = heur_manhattan

    generator_simulator = graphics.MazeGraphics if simulate_generation else None
    solver_simulator = graphics.MazeGraphics if simulate_solver else None

    # 0: BFS, 1: DFS, 2: Kruskal's, 3: Prim's
    Generator = 2
    # 0: BFS, 1: DFS, 2: UniformCost, 3: GreedyBFS, 4: A*, 5: IDA*
    Solver = 5

    print("----------------------------")

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

    print('Using {} to Generate the Maze'.format(genName))

    init_time = os.times()[0]
    maze.generate(Generator(debug, generator_simulator))
    gen_time = os.times()[0] - init_time

    print('Generator time: {}'.format(gen_time))
    print("----------------------------")

    if Solver == 0:
        SolverAlg = BFSSolver
        strategy = 'Breadth-First Search'
    elif Solver == 1:
        SolverAlg = DFSSolver
        strategy = 'Depth-First Search'
    elif Solver == 2:
        SolverAlg = UniformCostSolver
        strategy = 'Uniform-Cost Search'
    elif Solver == 3:
        SolverAlg = GreedyBFSSolver
        strategy = 'Greedy Best-First Search'
    elif Solver == 4:
        SolverAlg = AStarSolver
        strategy = 'A* Search'
    elif Solver == 5:
        SolverAlg = IDAStarSolver
        strategy = "IDA* Search"

    print('Search Strategy: {}'.format(strategy))

    if Solver > 2:
        init_time = os.times()[0]
        path = maze.solve(SolverAlg(heuristic, graphics = solver_simulator))
        search_time = os.times()[0] - init_time
    else:
        init_time = os.times()[0]
        path = maze.solve(SolverAlg(graphics = solver_simulator))
        search_time = os.times()[0] - init_time

    print('Search time: {}'.format(search_time))
    print('Solution cost: {}'.format(len(path)))
    print("----------------------------")

    if showGraphics:
        g = graphics.MazeGraphics(maze)
        g.run(path)
        g.top.mainloop()
