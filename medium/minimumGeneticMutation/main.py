class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        while queue:
            gene, n = queue.popleft()
            if gene == endGene:
                return n

            for i in range(len(gene)):
                for char in ["A", "C", "G", "T"]:
                    mutation = gene[:i] + char + gene[i + 1 :]
                    if mutation in bank:
                        queue.append((mutation, n + 1))
                        bank.remove(mutation)
        return -1
