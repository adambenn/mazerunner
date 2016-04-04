import random
from collections import deque
from Generators.generator import *

class DFSGenerator(Generator):
    def getNext(self, stack):
        return stack.pop()

    def run(self, maze):
        start, end = self.getEntranceExitCoords(maze)

        if self.debug:
            print("Starting DFS generation between cells {} and {}".format(start, end))
        stack = deque()
        visited = {}

        # Make the initial cell the current cell and mark it as visited
        self.setEntranceExit(maze, start, end)

        startCell = maze.getCell(start)
        visited[start] = True
        stack.append(startCell)

        while stack:
            current = self.getNext(stack)
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

        self.deleteRandomWalls(maze)
