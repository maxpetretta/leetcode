import random


class RandomizedSet:
    def __init__(self):
        self.values, self.dict = [], {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        index, last = self.dict[val], self.values[-1]
        self.values[index], self.dict[last] = last, index
        self.values.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
