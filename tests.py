import unittest

from maze import *


class CellTesting(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(5)

    def test_correct_neighbours_1(self):
        coord = (1, 1)
        neighbours = self.maze.getNeighbours(coord)

        self.assertEqual(len(neighbours), 4)
        self.assertIn(self.maze.getCell((0, 1)), neighbours)
        self.assertIn(self.maze.getCell((2, 1)), neighbours)
        self.assertIn(self.maze.getCell((1, 0)), neighbours)
        self.assertIn(self.maze.getCell((1, 2)), neighbours)

    def test_correct_neighbours_2(self):
        coord = (0, 0)
        neighbours = self.maze.getNeighbours(coord)

        self.assertEqual(len(neighbours), 2)
        self.assertIn(self.maze.getCell((0, 1)), neighbours)
        self.assertIn(self.maze.getCell((1, 0)), neighbours)

    def test_correct_neighbours_3(self):
        coord = (4, 1)
        neighbours = self.maze.getNeighbours(coord)

        self.assertEqual(len(neighbours), 3)
        self.assertIn(self.maze.getCell((3, 1)), neighbours)
        self.assertIn(self.maze.getCell((4, 0)), neighbours)
        self.assertIn(self.maze.getCell((4, 2)), neighbours)

    def test_adjacency_1(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((0, 1))
        self.assertTrue(cell1.isAdjacent(cell2))
        self.assertTrue(cell2.isAdjacent(cell1))

    def test_adjacency_2(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((3, 3))
        self.assertFalse(cell1.isAdjacent(cell2))
        self.assertFalse(cell2.isAdjacent(cell1))

    def test_adjacency_3(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((2, 2))
        self.assertFalse(cell1.isAdjacent(cell2))
        self.assertFalse(cell2.isAdjacent(cell1))

    def test_direction_1(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((0, 1))
        self.assertEqual(cell1.directionOfCell(cell2), 2)
        self.assertEqual(cell2.directionOfCell(cell1), 3)

    def test_direction_2(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((1, 0))
        self.assertEqual(cell1.directionOfCell(cell2), 0)
        self.assertEqual(cell2.directionOfCell(cell1), 1)

    def test_direction_3(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((3, 3))
        self.assertRaises(AssertionError, cell1.directionOfCell, cell2)
        self.assertRaises(AssertionError, cell2.directionOfCell, cell1)

    def test_remove_walls_1(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((1, 0))
        cell1.removeWallsBetweenCell(cell2)
        self.assertEqual(cell1.walls, [0, 1, 1, 1])
        self.assertEqual(cell2.walls, [1, 0, 1, 1])

    def test_remove_walls_2(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((0, 1))
        cell1.removeWallsBetweenCell(cell2)
        self.assertEqual(cell1.walls, [1, 1, 0, 1])
        self.assertEqual(cell2.walls, [1, 1, 1, 0])

    def test_remove_walls_3(self):
        cell1 = self.maze.getCell((1, 1))
        cell2 = self.maze.getCell((3, 3))
        self.assertRaises(AssertionError, cell1.removeWallsBetweenCell, cell2)

if __name__ == "__main__":
    unittest.main()