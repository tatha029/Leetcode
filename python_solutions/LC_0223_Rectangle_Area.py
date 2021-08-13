class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(width, height):
            return width * height if width > 0 and height > 0 else 0

        a_area = area(ax2 - ax1, ay2 - ay1)
        b_area = area(bx2 - bx1, by2 - by1)
        overlap = area(min(ax2, bx2) - max(ax1, bx1), min(ay2, by2) - max(ay1, by1))

        return a_area + b_area - overlap if overlap > 0 else a_area + b_area
