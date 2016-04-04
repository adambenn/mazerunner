import random
from collections import deque
from Generators.generator import *

class PrimsGenerator(Generator):
    def run(self, maze):
        start, end = self.getEntranceExitCoords(maze)

        self.setEntranceExit(maze, start, end)

        if self.debug:
            print("Starting Prim's generation between cells {} and {}".format(start, end))

        walls, visited = [], []

        cell = maze.getCell(start)
        visited.append(cell)

        for neighbour in maze.getNeighbours(start):
            walls.append((cell, neighbour))

        while walls != []:
            wall_index = random.randint(0, len(walls)-1)
            (cell, neighbour) = walls[wall_index]

            if neighbour not in visited:
                cell.removeWallsBetweenCell(neighbour)
                visited.append(neighbour)

                for n in maze.getNeighbours(neighbour.coordinate):
                    walls.append((neighbour, n))

            walls.pop(wall_index)

            if self.debug:
                print("Removed walls between {} and {}".format(cell, neighbour))
                print("Current maze:")
                print(maze.graphicalRepresentation())

        self.deleteRandomWalls(maze)
