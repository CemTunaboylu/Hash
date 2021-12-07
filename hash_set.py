# HashSet with separate chaining
# Do not handle growing the HashSet when there are too much collision and saturation
from bisect import bisect_left

class HashSet:
    MOD = 2 ** 61 - 1
    SIZE = 10_000
    def __init__(self, size = SIZE ):
        self.size = size * 2
        self.set = [None] * self.size
    def hash(self, data):
        if isinstance(data, str):
            i = _transform(self, data) % self.MOD
        else:
            i = data % self.MOD
        return i % self.size
    def _transform(self, s):
        i = int( "".join([ str(ord(x)) for x in s  ]) )
        return i

    def add(self, data):
        i = self.hash(data)
        chain = self.set[i]
        if chain:
            i_to_put = bisect_left(chain, data)
            check_here = i_to_put*(i_to_put == len(chain)-1) + (i_to_put+1)*(i_to_put < len(chain)-1)
            if chain[check_here] == data:
                pass # You already exist!
            else:
                chain.insert(i_to_put, data)
        else:
            self.set[i] = [data]

    def get(self, data):
        i = self.hash(data)
        chain = self.set[i]
        if not chain:
            return False
        pos = bisect_left(chain, data)
        check_here = pos*(pos==len(chain)-1) + (pos+1)*(pos<len(chain)-1)
        if not data == chain[check_here]:
            return False
        return True

    def remove(self, data):
        i = self.hash(data)
        chain = self.set[i]
        if not chain:
            return
        pos = bisect_left(chain, data)
        check_here = pos*(pos==len(chain)-1) + (pos+1)*(pos<len(chain)-1)
        if data == chain[check_here]:
            del chain[pos+1]

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

if __name__ == '_main__':
    int_test()
    str_test()
    small_size_test()
