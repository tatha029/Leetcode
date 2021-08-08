class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        state, maxStates = {}, 0
        stateToCell = {}
        repeat = False
        for i in range(n):
            cells = [0] + [int(i==j) for i,j in zip(cells+[0,0], [0,0]+cells)][2:-2] + [0]
            if str(cells) not in state:
                state[str(cells)] = i
                stateToCell[i] = cells
                maxStates += 1
            else:
                repeat = True
                break
        if not repeat:
            return cells
        return stateToCell[(n-1)%maxStates]
