import random
from collections import deque
from Generators.generator import *

class Node:
    def __init__(self, value, rank = 0, parent = None):
        self.value = value
        self.rank = rank
        self.parent = parent if parent else self

class DisjointSet:
    def __init__(self):
        self.sets = 0
        self.value_map = {}

    def createSet(self, value):
        st = Node(value)
        self.value_map[value] = st
        self.sets += 1
        return st

    def mergeSets(self, x, y):
        px = self.findSet(x)
        py = self.findSet(y)
        if px.rank > py.rank:
            py.parent = px
        else:
            px.parent = py

        if px.rank == py.rank:
            py.rank = px.rank + 1
        self.sets -= 1

    def findSet(self, x):
        while x.parent != x:
            x = x.parent
        return x

    def nodeForValue(self, val):
        return self.value_map[val]

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

        walls = {}
        disSet = DisjointSet()

        for y in range(len(maze.cells)):
            row = maze.cells[y]
            for x in range(len(row)):
                cell = row[x]
                n = disSet.createSet(cell) if not cell in disSet.value_map else disSet.value_map[cell]
                walls[n] = []
                for neighbour in maze.getNeighbours((x,y)):
                    if neighbour in disSet.value_map:
                        walls[n].append(disSet.nodeForValue(neighbour))
                    else:
                        walls[n].append(disSet.createSet(neighbour))

        while disSet.sets > 1:
            cell_node = random.choice(list(walls.keys()))
            neighbour_node = random.choice(walls[cell_node])

            set1 = disSet.findSet(cell_node)
            set2 = disSet.findSet(neighbour_node)

            if set1 != set2:

                cell_node.value.removeWallsBetweenCell(neighbour_node.value)

                disSet.mergeSets(cell_node, neighbour_node)

                walls[cell_node].remove(neighbour_node)
                walls[neighbour_node].remove(cell_node)

            if walls[cell_node] == []:
                del walls[cell_node]
            if walls[neighbour_node] == []:
                del walls[neighbour_node]

            if self.graphics:
                g.updatePath([])

            if self.debug:
                print("Removed walls between {} and {}".format(cell, neighbour))
                print("Current maze:")
                print(maze.graphicalRepresentation())

        self.deleteRandomWalls(maze, g)
