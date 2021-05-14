from dstplus.bitset import BitSet


def test_both_empty():
    bset1 = BitSet()
    bset2 = BitSet()
    bset = bset1.union(bset2)
    assert 0 not in bset
    assert 1 not in bset
    assert len(bset) == 0
    assert bset is not bset1
    assert bset is not bset2
    bset1.add(0)
    assert 0 not in bset
    bset2.add(1)
    assert 1 not in bset
    bset.add(2)
    assert 2 not in bset1
    assert 2 not in bset2


def test_singleton_empty():
    bset1 = BitSet()
    bset1.add(42)
    bset2 = BitSet()
    bset = bset1 | bset2
    assert 0 not in bset
    assert 1 not in bset
    assert 42 in bset
    assert len(bset) == 1


def test_empty_singleton():
    bset1 = BitSet()
    bset1.add(42)
    bset2 = BitSet()
    bset = bset2 | bset1
    assert 0 not in bset
    assert 1 not in bset
    assert 42 in bset
    assert len(bset) == 1


def test_same_singletons():
    bset1 = BitSet()
    bset1.add(42)
    bset2 = BitSet()
    bset2.add(42)
    bset = bset1 | bset2
    assert 0 not in bset
    assert 1 not in bset
    assert 42 in bset
    assert len(bset) == 1


def test_diff_singletons():
    bset1 = BitSet()
    bset1.add(42)
    bset2 = BitSet()
    bset2.add(3)
    bset = bset1 | bset2
    assert 0 not in bset
    assert 1 not in bset
    assert 42 in bset
    assert 3 in bset
    assert len(bset) == 2


def test_diff():
    bset1 = BitSet()
    bset1.add(42)
    bset1.add(2)
    bset2 = BitSet()
    bset2.add(3)
    bset2.add(2)
    bset = bset1 | bset2
    assert 0 not in bset
    assert 1 not in bset
    assert 42 in bset
    assert 3 in bset
    assert 2 in bset
    assert len(bset) == 3
    