"""Unit tests for agent-optical-table-parser."""
import unittest
from agent_optical_table_parser.parser import OpticalTableParser, TextCell

class TestTableParser(unittest.TestCase):
    def setUp(self):
        self.parser = OpticalTableParser()

    def test_grid_parsing(self):
        cells = [
            TextCell("A", 10, 10), TextCell("B", 100, 10),
            TextCell("1", 10, 50), TextCell("2", 100, 50)
        ]
        grid = self.parser.parse_to_grid(cells)
        self.assertEqual(len(grid), 2)
        self.assertEqual(grid[0], ["A", "B"])
        self.assertEqual(grid[1], ["1", "2"])

if __name__ == "__main__":
    unittest.main()
