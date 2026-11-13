"""Parses 2D spatially positioned text cells into structured tables."""
from typing import Dict, List, Optional, Tuple, Any

class TextCell:
    def __init__(self, text: str, x: int, y: int):
        self.text = text
        self.x = x
        self.y = y

class OpticalTableParser:
    """Groups spatial text cells into 2D grid tables based on row and column thresholds."""

    def __init__(self, row_tolerance: int = 15, col_tolerance: int = 50):
        self.row_tolerance = row_tolerance
        self.col_tolerance = col_tolerance

    def parse_to_grid(self, cells: List[TextCell]) -> List[List[str]]:
        if not cells:
            return []

        # Group cells by Y coordinate into rows
        sorted_by_y = sorted(cells, key=lambda c: c.y)
        rows: List[List[TextCell]] = []

        for cell in sorted_by_y:
            placed = False
            for r in rows:
                if abs(r[0].y - cell.y) <= self.row_tolerance:
                    r.append(cell)
                    placed = True
                    break
            if not placed:
                rows.append([cell])

        # Sort each row by X coordinate
        for r in rows:
            r.sort(key=lambda c: c.x)

        return [[c.text for c in r] for r in rows]

    def to_markdown(self, cells: List[TextCell]) -> str:
        grid = self.parse_to_grid(cells)
        if not grid:
            return ""

        lines = []
        header = grid[0]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * len(header)) + " |")
        for row in grid[1:]:
            lines.append("| " + " | ".join(row) + " |")

        return chr(10).join(lines)
