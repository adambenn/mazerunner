import random

class Generator:
    def __init__(self, debug = False):
        self.debug = debug

    def run(self, maze):
        pass

    def setEntranceExit(self, maze, entrance_coord, exit_coord):
        startCell = maze.getCell(entrance_coord)
        endCell = maze.getCell(exit_coord)

        maze.entrance = startCell
        maze.exit = endCell

        startCell.removeWall(2)
        endCell.removeWall(3)

    def deleteRandomWalls(self, maze):
        delete_count = (maze.size**2) // 2
        non_outside = [x[1:-1] for x in maze.cells[1:-1]]
        for i in range(delete_count):
            r = random.choice(non_outside)
            cell = random.choice(r)
            current_wall_dirs = [i for i in range(4) if cell.walls[i]]
            if current_wall_dirs:
                cell.removeWall(random.choice(current_wall_dirs))