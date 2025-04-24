class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)

        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(n):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index % n if total_tank >= 0 else -1


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
