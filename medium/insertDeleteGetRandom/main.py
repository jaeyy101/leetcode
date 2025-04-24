import random

class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.setIndexes = []

    def insert(self, val: int) -> bool:
        if not_exist := val not in self.set:
            self.set[val] = len(self.setIndexes)
            self.setIndexes.append(val)

        return not_exist
        

    def remove(self, val: int) -> bool:
        exists = val in self.set
        if exists:
            index = self.set[val]
            lastNum = self.setIndexes[-1]
            self.setIndexes[index] = lastNum
            self.setIndexes.pop()
            self.set[lastNum] = index
            del self.set[val]

        return exists

    def getRandom(self) -> int:
        return random.choice(self.setIndexes)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()