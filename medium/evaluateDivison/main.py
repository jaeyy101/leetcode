from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = defaultdict(dict)

        for i in range(len(values)):
            num, den = equations[i]
            weight = values[i]
            graph[num][den] = weight
            graph[den][num] = 1 / weight

        def go_from_to(x, y):
            stack = [(x, 1)]
            visited = set()

            while stack:
                curr, w = stack.pop()
                if curr in visited:
                    continue
                if y in graph[curr]:
                    return w * graph[curr][y]
                for key, value in graph[curr].items():
                    stack.append((key, w * value))
                visited.add(curr)
            return -1

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            elif a == b:
                ans.append(1.0)
            else:
                res = go_from_to(a, b)
                if res == -1:
                    reversed_res = go_from_to(b, a)
                    if reversed_res != -1:
                        res = 1 / reversed_res
                ans.append(res)
        return ans

    def calcEquation1(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:

        graph = defaultdict(dict)
        for i in range(len(equations)):
            numerator, denominator = equations[i]
            val = values[i]
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1 / val

        def query(nu, de):

            nonlocal graph
            seen = set()

            if nu not in graph or de not in graph:
                return -1

            def dfs(node, val_so_far):
                seen.add(node)
                if node == de:
                    return val_so_far

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        result = dfs(neighbor, val_so_far * graph[node][neighbor])
                        if result != -1:
                            return result

                return -1

            return dfs(nu, 1)

        return [query(nu, de) for nu, de in queries]


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.weight = {}

    def find(self, x):
        if x != self.parent[x]:
            orig_parent = self.parent[x]
            self.parent[x], w = self.find(orig_parent)
            self.weight[x] *= w
        return self.parent[x], self.weight[x]

    def union(self, x, y, value):  # x / y = value
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
        if y not in self.parent:
            self.parent[y] = y
            self.weight[y] = 1.0

        rootX, weightX = self.find(x)
        rootY, weightY = self.find(y)

        if rootX != rootY:
            self.parent[rootX] = rootY
            # Adjust weight to maintain x / y = value
            self.weight[rootX] = (value * weightY) / weightX

    def isConnected(self, x, y):
        if x not in self.parent or y not in self.parent:
            return -1.0
        rootX, weightX = self.find(x)
        rootY, weightY = self.find(y)
        if rootX != rootY:
            return -1.0
        return weightX / weightY


class Solulu:
    def calcEquation(self, equations, values, queries):
        uf = UnionFind()

        # Step 1: Union all equations
        for (a, b), val in zip(equations, values):
            uf.union(a, b, val)

        # Step 2: Process queries
        result = []
        for a, b in queries:
            result.append(uf.isConnected(a, b))
        return result


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(Solulu().calcEquation(equations, values, queries))
