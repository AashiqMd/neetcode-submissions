class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(("0000",0))
        deadEndSet = set(deadends)

        while queue:
            curCode, minTurns = queue.popleft()
            if curCode == target:
                return minTurns
            if curCode in deadEndSet:
                continue

            deadEndSet.add(curCode)
            
            for i in range(4):
                temp = curCode
                up = (int(temp[i]) + 1) % 10
                down = (int(temp[i]) - 1) % 10

                queue.append((temp[:i] + str(up) + temp[i+1:], minTurns + 1))
                queue.append((temp[:i] + str(down) + temp[i+1:], minTurns + 1))

        return -1