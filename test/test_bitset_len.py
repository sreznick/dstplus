from dstplus.bitset import BitSet
import random


def test_empty():
    bset = BitSet()
    assert len(bset) == 0


def test_single():
    bset = BitSet()
    bset.add(42)
    assert len(bset) == 1


def test_two_elems():
    bset = BitSet()
    bset.add(42)
    bset.add(2)
    assert len(bset) == 2


def test_repeated():
    bset = BitSet()
    bset.add(42)
    bset.add(42)
    assert len(bset) == 1


def test_remove():
    bset = BitSet()
    bset.add(42)
    bset.remove(42)
    assert len(bset) == 0
    bset.remove(42)
    assert len(bset) == 0
    bset.add(42)
    bset.add(2)
    bset.remove(42)
    assert len(bset) == 1
    bset.remove(2)
    assert len(bset) == 0


def test_random():
    random.seed(32)
    add = 0
    remove = 1
    opvals = [(random.sample((add, remove), 1)[0], random.randrange(100)) for _ in range(1000)]
    s_py = set()
    s_bitset = BitSet()
    for op, value in opvals:
        if op == add:
            s_py.add(value)
            s_bitset.add(value)
        elif op == remove:
            if value in s_py:
                s_py.remove(value)
            s_bitset.remove(value)
        assert len(s_py) == len(s_bitset)
