class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        self.weight = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], w = self.find(self.parent[x])
            self.weight[x] *= w
        return self.parent[x], self.weight[x]

    def union(self, x, y, value):
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
            self.weight[rootX] = (value * weightY) / weightX

    def isConnected(self, x, y):
        if x not in self.parent or y not in self.parent:
            return -1.0
        rootX, weightX = self.find(x)
        rootY, weightY = self.find(y)
        if rootX != rootY:
            return -1.0
        return weightX / weightY


rates = [
    ["USD", "EUR", 0.85],
    ["EUR", "JPY", 130],
    ["JPY", "GBP", 0.0068],
    ["GBP", "INR", 100],
]

uf = UnionFind()
for num, den, rate in rates:
    uf.union(num, den, rate)

print(uf.isConnected("INR", "JPY"))
