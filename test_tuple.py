import pytest


def test_append():
    t = 1, 2
    try:
        assert t.append(3)
    except AttributeError:
        pass


def test_in():
    t = 1, 2
    assert 1 in t


@pytest.mark.parametrize(
    "items,count",
    [((1, 1), 2),
    ((), 0)]
)
def test_count_of_one(items, count):
    assert items.count(1) == count

