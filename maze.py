from functools import reduce

'''
A Cell in a maze, has 4 walls which can be removed
'''
class Cell:
    def __init__(self, coordinate):
        self.walls = [1] * 4
        self.coordinate = coordinate

    def __validateDirection(self, direction):
        assert direction in range(0, 4), "{} is not a valid direction for a wall".format(direction)

    def removeWall(self, direction):
        '''
        Removes wall in specified direction
        :param direction: 0: Up, 1: Down, 2: Left, 3: Right
        '''
        self.__validateDirection(direction)
        self.walls[direction] = 0

    def hasWall(self, direction):
        '''
        :param direction: 0: Up, 1: Down, 2: Left, 3: Right
        :return: Returns True if specified direction has a wall, False otherwise
        '''
        self.__validateDirection(direction)
        return self.walls[direction]

    def isAdjacent(self, cell):
        return abs(cell.coordinate[0] - cell.coordinate[0]) <= 1 and\
               abs(cell.coordinate[1] - cell.coordinate[1]) <= 1 and \
               (cell.coordinate[0] == self.coordinate[0] or cell.coordinate[1] == self.coordinate[1])

    def directionOfCell(self, cell):
        '''
        Returns the direction of an adjacent cell
        :param cell: A Cell which must be adjacent (up down left or right) *not diagonal*
        :return: 0: Up, 1: Down, 2: Left, 3: Right
        '''
        assert self.isAdjacent(cell), "Can't check direction between {} and non adjacent cell {}".format(self, cell)
        if cell.coordinate[0] - self.coordinate[0] == 1:
            return 3 # right
        elif cell.coordinate[0] - self.coordinate[0] == -1:
            return 2 # left
        elif cell.coordinate[1] - self.coordinate[1] == 1:
            return 1 # bottom
        elif cell.coordinate[1] - self.coordinate[1] == -1:
            return 0 # top
        else:
            raise Exception("All possible directions exhausted")

    def removeWallsBetweenCell(self, cell):
        assert self.isAdjacent(cell), "Can't remove walls between {} and non adjacent cell {}".format(self, cell)
        self.removeWall(self.directionOfCell(cell))
        cell.removeWall(cell.directionOfCell(self))

    def hasWallBetween(self, cell):
        assert self.isAdjacent(cell), "Can't check for walls between {} and non adjacent cell {}".format(self, cell)
        return self.hasWall(self.directionOfCell(cell)) or cell.hasWall(cell.directionOfCell(self))

    def __repr__(self):
        walls = ["Top", "Bottom", "Left", "Right"]
        walls = [walls[i] for i in range(len(walls)) if self.walls[i]]
        return "Cell at coordinate {}, with walls {}".format(self.coordinate, ", ".join(walls))

    def graphicalRepresentation(self):
        out = ""
        if self.walls[2]:
            out += "|"
        else:
            out += " "

        if self.walls[0] and not self.walls[1]:
            out += u"\u203E"
        elif self.walls[1] and not self.walls[0]:
            out += "_"
        elif self.walls[0] and self.walls[1]:
            out += "I"
        else:
            out += " "

        if self.walls[3]:
            out += "|"
        else:
            out += " "

        return out

class Maze:
    def __init__(self, size):
        self.size = size
        self.cells = []

        self.entrance = None
        self.exit = None

        for y in range(self.size):
            self.cells.append([])
            for x in range(self.size):
                self.cells[y].append(Cell((x, y)))

    def __validateCoordinate(self, coordinate):
        # verify it is a size two tuple of ints
        assert isinstance(coordinate, tuple) and len(coordinate) == 2 and \
               reduce(lambda x,y: x and y, [isinstance(x, int) for x in coordinate]), \
            "{} is not a valid coordinate, must be tuple of form (Integer, Integer)".format(coordinate)

        # verify it within the range of the maze
        inRange = lambda x: x >= 0 and x < self.size
        assert inRange(coordinate[0]) and inRange(coordinate[1]), \
            "{} is not a valid coordinate in the maze".format(coordinate)

    def generate(self, generator):
        generator.run(self)

    def solve(self, solver):
        return solver.solve(self)

    def getCell(self, coordinate):
        self.__validateCoordinate(coordinate)
        return self.cells[coordinate[1]][coordinate[0]]

    def getNeighbours(self, coordinate):
        self.__validateCoordinate(coordinate)
        neighbours = []

        if coordinate[0] != 0:
            neighbours.append(self.getCell((coordinate[0] - 1, coordinate[1])))
        if coordinate[0] != self.size - 1:
            neighbours.append(self.getCell((coordinate[0] + 1, coordinate[1])))
        if coordinate[1] != 0:
            neighbours.append(self.getCell((coordinate[0], coordinate[1] - 1)))
        if coordinate[1] != self.size - 1:
            neighbours.append(self.getCell((coordinate[0], coordinate[1] + 1)))

        return neighbours

    def getNeighbourInDirection(self, coordinate, direction):
        self.__validateCoordinate(coordinate)
        cell = self.getCell(coordinate)
        assert direction in range(4)

        if direction == 0:
            if coordinate[1] > 0:
                return self.getCell((coordinate[0], coordinate[1] - 1))
            else:
                raise Exception("Invalid direction {} for cell {}".format(direction, cell))
        elif direction == 1:
            if coordinate[1] < self.size - 1:
                return self.getCell((coordinate[0], coordinate[1] + 1))
            else:
                raise Exception("Invalid direction {} for cell {}".format(direction, cell))
        elif direction == 2:
            if coordinate[0] > 0:
                return self.getCell((coordinate[0] - 1, coordinate[1]))
            else:
                raise Exception("Invalid direction {} for cell {}".format(direction, cell))
        elif direction == 3:
            if coordinate[0] < self.size - 1:
                return self.getCell((coordinate[0] + 1, coordinate[1]))
            else:
                raise Exception("Invalid direction {} for cell {}".format(direction, cell))

    def graphicalRepresentation(self):
        out = ""
        for y in range(self.size):
            for x in range(self.size):
                out += self.cells[y][x].graphicalRepresentation()
            out += "\n"
        return out

