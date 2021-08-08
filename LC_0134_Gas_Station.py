class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if solution exists
        if sum(gas) < sum(cost):
            return -1
        min_pt, min_gas = 0, 0
        cur_gas = 0
        for i in range(len(gas)):
            cur_gas = cur_gas + gas[i] - cost[i]
            if cur_gas < min_gas:
                min_pt, min_gas = i+1, cur_gas
        return min_pt
