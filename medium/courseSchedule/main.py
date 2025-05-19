from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            if not a in graph:
                graph[a] = []
            graph[b].append(a)

        in_degree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

        count = 0
        queue = deque([node for node in graph if in_degree[node] == 0])
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == len(graph.keys())


graph = {0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4], 4: []}
in_degree = {node: 0 for node in graph}

for node in graph:
    for neighbor in graph[node]:
        in_degree[neighbor] += 1

top_sort = []
queue = deque([node for node in in_degree if in_degree[node] == 0])
while queue:
    node = queue.popleft()
    top_sort.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)


def is_cyclic(numCourses, prerequisites):
    graph = {0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [4], 4: []}
    # for p, q in prerequisites:
    #     if q not in graph:
    #         graph[q] = []
    #     graph[p].append(q)

    visited = set()
    recStack = set()

    def is_cyclic_util(node):
        if node in recStack:
            return True

        if node in visited:
            return False

        visited.add(node)
        recStack.add(node)

        for neighbor in graph[node]:
            if is_cyclic_util(neighbor):
                return True

        recStack.remove(node)
        return False

    for node in graph:
        if node not in visited and is_cyclic_util(node):
            return True
    return False


print(is_cyclic(2, 2))
