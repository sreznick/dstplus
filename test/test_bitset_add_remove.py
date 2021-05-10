from dstplus.bitset import BitSet

def test_add():
    bset = BitSet()
    assert 0 not in bset
    assert 1 not in bset
    assert 34 not in bset

    bset.add(0)
    assert 0 in bset
    assert 1 not in bset
    assert 34 not in bset

    bset.add(1)
    assert 0 in bset
    assert 1 in bset
    assert 34 not in bset

    bset.add(34)
    assert 0 in bset
    assert 1 in bset
    assert 34 in bset


def test_remove():
    bset = BitSet()
    bset.add(0)
    bset.add(1)
    bset.add(34)
    assert 0 in bset
    assert 1 in bset
    assert 34 in bset

    bset.remove(1)
    assert 0 in bset
    assert 1 not in bset
    assert 34 in bset

    bset.remove(0)
    assert 0 not in bset
    assert 1 not in bset
    assert 34 in bset

    bset.remove(34)
    assert 0 not in bset
    assert 1 not in bset
    assert 34 not in bset


def test_add_double():
    bset = BitSet()
    assert 5 not in bset
    bset.add(5)
    assert 5 in bset
    bset.add(5)
    assert 5 in bset
    bset.remove(5)
    assert 5 not in bset


def test_remove_double():
    bset = BitSet()
    bset.add(5)
    assert 5 in bset
    bset.remove(5)
    assert 5 not in bset
    bset.remove(5)
    assert 5 not in bset
    bset.add(5)
    assert 5 in bset


def test_add_remove_mix():
    bset = BitSet()
    bset.add(5)
    bset.add(3)
    assert 3 in bset
    assert 5 in bset
    bset.remove(3)
    assert 3 not in bset
    assert 5 in bset
    bset.add(3)
    assert 3 in bset
    assert 5 in bset
    bset.add(7)
    assert 3 in bset
    assert 5 in bset
    assert 7 in bset
    bset.remove(5)
    assert 3 in bset
    assert 5 not in bset
    assert 7 in bset
