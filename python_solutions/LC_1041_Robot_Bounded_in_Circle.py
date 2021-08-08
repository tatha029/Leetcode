class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def move(vec):
            if vec[2] == 0: # north
                vec[1] += 1
            elif vec[2] == 90: # west
                vec[0] -= 1
            elif vec[2] == 180: # south
                vec[1] -= 1
            else: # east
                vec[0] += 1

        vec = [0,0,0] # (x,y) and dirn
        for i in instructions:
            if i == 'L':
                vec[2] = (vec[2] - 90)%360
            elif i == 'R':
                vec[2] = (vec[2] + 90)%360
            else: # i == 'G'
                move(vec)

        return (vec[0] == 0 and vec[1] == 0) or vec[2] != 0
