from dstplus.bitset import BitSet


def test_clear():
    bset = BitSet()
    bset.add(0)
    bset.add(1)
    bset.add(34)
    assert 0 in bset
    assert 1 in bset
    assert 2 not in bset
    assert 34 in bset

    bset.clear()
    assert 0 not in bset
    assert 1 not in bset
    assert 2 not in bset
    assert 34 not in bset


def test_clear_double():
    bset = BitSet()
    bset.add(0)
    bset.add(1)
    bset.add(34)

    bset.clear()
    bset.clear()
    assert 0 not in bset
    assert 1 not in bset
    assert 2 not in bset
    assert 34 not in bset


def test_on_empty():
    bset = BitSet()
    bset.clear()
    assert 0 not in bset
    assert 1 not in bset
    assert 2 not in bset
    assert 34 not in bset
