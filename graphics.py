import tkinter

class MazeGraphics:
    CELL_SIZE = 15
    OFFSET = 50
    WIDTH = 480
    HEIGHT = 320
    def __init__(self, maze):
        self.maze = maze

    def __drawCell(self, canvas, cell, path):
        c = (self.OFFSET + (cell.coordinate[0] * self.CELL_SIZE), self.OFFSET + (cell.coordinate[1] * self.CELL_SIZE))
        # top side
        if cell.hasWall(0):
            canvas.create_line(c[0], c[1], c[0] + self.CELL_SIZE, c[1])
        # left side
        if cell.hasWall(2):
            canvas.create_line(c[0], c[1], c[0], c[1] + self.CELL_SIZE)
        # bottom side
        if cell.hasWall(1):
            canvas.create_line(c[0], c[1] + self.CELL_SIZE, c[0] + self.CELL_SIZE, c[1] + self.CELL_SIZE)
        # right side
        if cell.hasWall(3):
            canvas.create_line(c[0] + self.CELL_SIZE, c[1], c[0] + self.CELL_SIZE, c[1] + self.CELL_SIZE)

        if path and cell in path:
            ind = path.index(cell)
            ind -= 1
            if ind >= 0:
                last = path[ind]
                path_c = (self.OFFSET + (last.coordinate[0] * self.CELL_SIZE), self.OFFSET + (last.coordinate[1] * self.CELL_SIZE))
                path_c = (path_c[0] + self.CELL_SIZE // 2, path_c[1] + self.CELL_SIZE // 2)
                c = (c[0] + self.CELL_SIZE // 2, c[1] + self.CELL_SIZE // 2)
                canvas.create_line(path_c[0], path_c[1], c[0], c[1], fill = "red")
            else:
                c = (c[0] + self.CELL_SIZE // 2, c[1] + self.CELL_SIZE // 2)
                canvas.create_line(c[0] - self.CELL_SIZE, c[1], c[0], c[1], fill = "red")

            if cell == self.maze.exit:
                canvas.create_line(c[0], c[1], c[0] + self.CELL_SIZE, c[1], fill = "red")

    def __drawMaze(self, canvas, path):
        for y in range(self.maze.size):
            for x in range(self.maze.size):
                self.__drawCell(canvas, self.maze.cells[y][x], path)

    def updatePath(self, path):
        self.canvas.delete("all")
        self.__drawMaze(self.canvas, path)
        self.top.update()

    def run(self, path = []):
        self.top = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.top, height = self.HEIGHT, width = self.WIDTH)
        self.canvas.pack()

        self.__drawMaze(self.canvas, path)
        self.top.update()