import random
from collections import deque
from Generators.generator import *

class PrimsGenerator(Generator):
    def run(self, maze):
        start, end = self.getEntranceExitCoords(maze)

        self.setEntranceExit(maze, start, end)

        if self.debug:
            print("Starting Prim's generation between cells {} and {}".format(start, end))

        g = None
        if self.graphics:
            g = self.graphics(maze)
            g.run([])

        walls, visited = [], {}

        cell = maze.getCell(start)
        visited[cell.coordinate] = True

        for neighbour in maze.getNeighbours(start):
            walls.append((cell, neighbour))

        while walls != []:
            wall_index = random.randint(0, len(walls)-1)
            (cell, neighbour) = walls[wall_index]

            if neighbour.coordinate not in visited:
                cell.removeWallsBetweenCell(neighbour)
                visited[neighbour.coordinate] = True
                if g:
                    g.updatePath([])

                for n in maze.getNeighbours(neighbour.coordinate):
                    walls.append((neighbour, n))

            walls.pop(wall_index)

            if self.debug:
                print("Removed walls between {} and {}".format(cell, neighbour))
                print("Current maze:")
                print(maze.graphicalRepresentation())

        self.deleteRandomWalls(maze, g)
