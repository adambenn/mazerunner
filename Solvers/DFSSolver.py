from collections import deque
from Solvers.solver import *
import time

class DFSSolver(Solver):
    def solve(self, maze):
        if (not maze.exit) or (not maze.entrance):
            print("Maze exit or entrance missing")
            return []
        if self.graphics:
            g = self.graphics(maze)
            g.run([])

        stack = deque()
        stack.append(maze.entrance)
        visited = {}

        path = []
        while stack:
            current = stack.pop()
            visited[current.coordinate] = True

            if path == [] or path[-1] != current:
                # when DFS goes down a dead end and reverses, the node in which it
                # branched off down that path will still be on the path. so this
                # prevents duplicates
                path.append(current)

            if self.graphics:
                g.updatePath(path)
                #time.sleep(self.UPDATE_DELAY)

            if self.isGoal(maze, current):
                return path

            neighbours = maze.getNeighbours(current.coordinate)
            # non-visited neighbours with no wall between us
            neighbours = [x for x in neighbours if not x.coordinate in visited and not current.hasWallBetween(x)]

            if neighbours:
                stack.append(current)
                stack.append(neighbours[0])
            else:
                path.pop()

        print("No path found between {} and {}".format(maze.entrance, maze.exit))
        return []