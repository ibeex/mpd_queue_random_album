from mpdrandom.mpdrandom import get_cache_size, enforce_cache_size


def test_larger():
    assert 100 == get_cache_size(1000, 10)


def test_smaler():
    assert 10 == get_cache_size(100, 10)


def test_size():
    cache = list(range(10))
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == enforce_cache_size(10, cache)
    assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == enforce_cache_size(11, cache)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9] == enforce_cache_size(9, cache)
