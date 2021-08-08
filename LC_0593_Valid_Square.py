class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def sqDist(x1, x2):
            return (x1[0]-x2[0])**2 + (x1[1]-x2[1])**2

        pts = sorted([p1, p2, p3, p4], key=lambda x: (x[0], x[1]))
        all_sides_eq = (sqDist(pts[0], pts[1]) == sqDist(pts[1], pts[3])) and \
                       (sqDist(pts[1], pts[3]) == sqDist(pts[3], pts[2])) and \
                       (sqDist(pts[3], pts[2]) == sqDist(pts[2], pts[0])) and \
                       (sqDist(pts[2], pts[0]) == sqDist(pts[0], pts[1]))

        all_diags_eq = (sqDist(pts[0], pts[3]) == sqDist(pts[1], pts[2]))
        return all_sides_eq and all_diags_eq and (sqDist(pts[2], pts[0]) != 0)
