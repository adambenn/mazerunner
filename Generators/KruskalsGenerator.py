import random
from collections import deque
from Generators.generator import *

class KruskalsGenerator(Generator):
    def run(self, maze):
        start, end = self.getEntranceExitCoords(maze)

        self.setEntranceExit(maze, start, end)

        if self.debug:
            print("Starting Kruskal generation between cells {} and {}".format(start, end))

        g = None
        if self.graphics:
            g = self.graphics(maze)
            g.run([])

        walls, sets = {}, []

        for y in range(len(maze.cells)):
            row = maze.cells[y]
            for x in range(len(row)):
                cell = row[x]
                sets.append({cell})
                walls[cell] = []
                for neighbour in maze.getNeighbours((x,y)):
                    walls[cell].append(neighbour)

        while len(sets) != 1:
            cell = random.choice(list(walls.keys()))
            neighbour = random.choice(walls[cell])

            set1 = [s for s in sets if cell in s][0]
            set2 = [s for s in sets if neighbour in s][0]

            if set1 != set2:

                cell.removeWallsBetweenCell(neighbour)

                new_set = set1.union(set2)
                sets.remove(set1)
                sets.remove(set2)
                sets.append(new_set)

            walls[cell].remove(neighbour)
            walls[neighbour].remove(cell)

            if walls[cell] == []:
                del walls[cell]
            if walls[neighbour] == []:
                del walls[neighbour]

            if self.graphics:
                g.updatePath([])

            if self.debug:
                print("Removed walls between {} and {}".format(cell, neighbour))
                print("Current maze:")
                print(maze.graphicalRepresentation())

        self.deleteRandomWalls(maze, g)
