from Solvers.solver import *
import heapq

class CostCellWrapper:
    def __init__(self, cell, cost, dist, predecessor = None):
        self.cell = cell
        self.cost = cost
        self.dist = dist
        self.predecessor = predecessor

    def __lt__(self, other):
        return self.cost < other.cost

class AStarSolver(HeuristicSolver):
    def solve(self, maze):
        if (not maze.exit) or (not maze.entrance):
            print("Maze exit or entrance missing")
            return []
        if self.graphics:
            g = self.graphics(maze)
            g.run([])
        visited = {}

        h = []
        heapq.heappush(h, CostCellWrapper(maze.entrance, 0, 0))
        while h:
            cost_cell = heapq.heappop(h)
            dist = cost_cell.dist
            current = cost_cell.cell
            visited[current.coordinate] = True

            if self.graphics:
                path = []
                c_cell = cost_cell
                while c_cell.predecessor:
                    path.append(c_cell.cell)
                    c_cell = c_cell.predecessor
                path.append(c_cell.cell)
                g.updatePath(list(reversed(path)))
                #time.sleep(self.UPDATE_DELAY)

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
                    heapq.heappush(h, CostCellWrapper(n, self.cost(dist, maze, n), dist + 1, cost_cell))

        print("No path found between {} and {}".format(maze.entrance, maze.exit))
        return []
