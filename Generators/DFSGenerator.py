import random
from collections import deque
from Generators.generator import *

class DFSGenerator(Generator):
    def run(self, maze):
        start = (0, random.randint(0, maze.size - 1))
        end = (maze.size - 1, random.randint(0, maze.size - 1))

        if self.debug:
            print("Starting DFS generation between cells {} and {}".format(start, end))
        stack = deque()
        visited = {}

        # Make the initial cell the current cell and mark it as visited
        startCell = maze.getCell(start)
        endCell = maze.getCell(end)

        maze.entrance = startCell
        maze.exit = endCell

        startCell.removeWall(2)
        endCell.removeWall(3)

        visited[start] = True
        stack.append(startCell)

        while stack:
            current = stack.pop()
            neighbours = maze.getNeighbours(current.coordinate)
            # get unvisited neighbours
            neighbours = [x for x in neighbours if not x.coordinate in visited]

            if neighbours:
                stack.append(current)
                nextCell = random.choice(neighbours)

                current.removeWallsBetweenCell(nextCell)
                visited[nextCell.coordinate] = True
                stack.append(nextCell)

                if self.debug:
                    print("Removed walls between {} and {}".format(current, nextCell))
                    print("Current maze:")
                    print(maze.graphicalRepresentation())
