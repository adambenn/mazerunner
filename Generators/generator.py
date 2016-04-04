import random

class Generator:
    def __init__(self, debug = False, graphics = None):
        self.debug = debug
        self.graphics = graphics

    def run(self, maze):
        pass

    def setEntranceExit(self, maze, entrance_coord, exit_coord):
        startCell = maze.getCell(entrance_coord)
        endCell = maze.getCell(exit_coord)

        maze.entrance = startCell
        maze.exit = endCell

        startCell.removeWall(2)
        endCell.removeWall(3)

    def deleteRandomWalls(self, maze, g = None):
        delete_count = (maze.size**2) // 10
        non_outside = [x[1:-1] for x in maze.cells[1:-1]]
        for i in range(delete_count):
            r = random.choice(non_outside)
            cell = random.choice(r)
            current_wall_dirs = [j for j in range(4) if cell.walls[j]]
            if current_wall_dirs:
                cell.removeWallsBetweenCell(maze.getNeighbourInDirection(cell.coordinate, random.choice(current_wall_dirs)))
                if g:
                    g.updatePath([])

    def getEntranceExitCoords(self, maze):
        start = (0, random.randint(0, maze.size - 1))
        end = (maze.size - 1, random.randint(0, maze.size - 1))
        return start, end
