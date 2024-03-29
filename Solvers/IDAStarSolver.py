from Solvers.solver import HeuristicSolver
from Solvers.AStarSolver import CostCellWrapper
from collections import deque

class IDAStarSolver(HeuristicSolver):
    def solve(self, maze):
        if self.graphics:
            g = self.graphics(maze)
            g.run([])

        min_cost = 1
        while True:
            visited = {}
            start = maze.entrance
            bound = min_cost
            stack = deque()
            path = []

            stack.append(CostCellWrapper(start, 0, 0))

            min_cost = float("inf")
            while stack:
                cost_cell = stack.pop()
                dist = cost_cell.dist
                cost = cost_cell.cost
                current = cost_cell.cell
                visited[current.coordinate] = True

                if cost > bound:
                    if cost < min_cost:
                        min_cost = cost
                    continue

                if path == [] or path[-1] != current:
                    path.append(current)

                if self.isGoal(maze, current):
                    return path

                neighbours = maze.getNeighbours(current.coordinate)
                # non-visited neighbours with no wall between us
                neighbours = [x for x in neighbours if not x.coordinate in visited and not current.hasWallBetween(x)]

                if neighbours:
                    if self.graphics:
                        g.updatePath(path)
                        #time.sleep(self.UPDATE_DELAY)

                    cheapest = min(neighbours, key = lambda x: self.cost(dist, maze, x))
                    stack.append(cost_cell)
                    stack.append(CostCellWrapper(cheapest, self.cost(dist, maze, cheapest), dist + 1))
                else:
                    path.pop()

        print("No path found between {} and {}".format(maze.entrance, maze.exit))
        return []