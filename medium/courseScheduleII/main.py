from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        top_sort = []
        while queue:
            node_index = queue.popleft()
            top_sort.append(node_index)

            for neighbor_index in graph[node_index]:
                in_degree[neighbor_index] -= 1
                if in_degree[neighbor_index] == 0:
                    queue.append(neighbor_index)
        return top_sort if len(top_sort) == numCourses else []
