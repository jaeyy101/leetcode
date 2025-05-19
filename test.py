from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses


print(Solution().canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
