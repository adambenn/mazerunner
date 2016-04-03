from Solvers.solver import *
import heapq

class CostCellWrapper:
    def __init__(self, cell, cost, predecessor = None):
        self.cell = cell
        self.cost = cost
        self.predecessor = predecessor

    def __lt__(self, other):
        return self.cost < other.cost

class UniformCostSolver(Solver):
    def solve(self, maze):
        if (not maze.exit) or (not maze.entrance):
            print("Maze exit or entrance missing")
            return []
        visited = {}

        h = []
        heapq.heappush(h, CostCellWrapper(maze.entrance, 0))
        while h:
            cost_cell = heapq.heappop(h)
            dist = cost_cell.cost
            current = cost_cell.cell
            visited[current.coordinate] = True

            if self.isGoal(maze, current):
                path = []
                while cost_cell.predecessor:
                    path.append(cost_cell.cell)
                    cost_cell = cost_cell.predecessor
                path.append(cost_cell.cell)
                return list(reversed(path))

            neighbours = maze.getNeighbours(current.coordinate)
            # non-visited neighbours with no wall between us
            neighbours = [x for x in neighbours if not x.coordinate in visited and not current.hasWallBetween(x)]

            if neighbours:
                for n in neighbours:
                    heapq.heappush(h, CostCellWrapper(n, dist + 1, cost_cell))

        print("No path found between {} and {}".format(maze.entrance, maze.exit))
        return []