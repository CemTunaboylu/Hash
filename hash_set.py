# HashSet with separate chaining
# Do not handle growing the HashSet when there are too much collision and saturation

class HashSet:
    MOD = 2 ** 61 - 1
    SIZE = 10_000
    def __init__(self, size = SIZE ):
        self.size = size * 2
        self.set = [ set() for _ in range(self.size)]
    def hash(self, data):
        if isinstance(data, str):
            i = self._transform(data) % self.MOD
        else:
            i = data % self.MOD
        return i % self.size
    def _transform(self, s):
        i = int( "".join([ str(ord(x)) for x in s  ]) )
        return i

    def add(self, data):
        i = self.hash(data)
        self.set[i].add(data)

    def get(self, data):
        i = self.hash(data)
        return data in self.set[i]

    def remove(self, data):
        i = self.hash(data)
        if data in self.set[i]:
            self.set[i].remove(data)

def int_test():
    hs = HashSet()
    hs.add(123)
    hs.add(124)
    hs.add(145)
    hs.add(138)
    hs.add(2**50)
    r = hs.get(145)
    assert r == True
    r = hs.get(10)
    assert r == False

def str_test():
    hs = HashSet()
    from itertools import permutations
    ss = list(permutations("ABCD"))
    ss = [ "".join(t) for t in ss ]
    for s in ss:
        hs.add(s)

    for s in ss:
        assert hs.get(s) == True

    assert hs.get("X") == False

def small_size_test():
    hs = HashSet(10)
    r = range(1000)
    for i in r:
        hs.add(i)

    for i in r:
        assert hs.get(i) == True
    assert hs.get(-1) == False

if __name__ == '__main__':
    int_test()
    str_test()
    small_size_test()
