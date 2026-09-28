import random

import pytest

from algorithms import ALGORITHMS

NAMES = [name for name, _ in ALGORITHMS.values()]
FUNCTIONS = [fn for _, fn in ALGORITHMS.values()]


@pytest.mark.parametrize("sort", FUNCTIONS, ids=NAMES)
@pytest.mark.parametrize("ascending", [True, False], ids=["ascending", "descending"])
@pytest.mark.parametrize("seed", range(25))
def test_every_algorithm_sorts_in_the_requested_direction(sort, ascending, seed):
    rng = random.Random(seed)
    values = [rng.randint(1, 30) for _ in range(rng.randint(0, 40))]
    expected = sorted(values, reverse=not ascending)

    for _ in sort(values, ascending):
        pass

    assert values == expected


@pytest.mark.parametrize("sort", FUNCTIONS, ids=NAMES)
def test_every_step_highlights_only_valid_indices(sort):
    values = [5, 3, 8, 1, 9, 2]

    for step in sort(values, True):
        assert step, "each step highlights something to draw"
        assert all(0 <= i < len(values) for i in step)
        assert set(step.values()) <= {"compare", "swap", "pivot", "placed"}


@pytest.mark.parametrize("sort", FUNCTIONS, ids=NAMES)
def test_lists_of_equal_values_and_single_items_are_handled(sort):
    for values in ([7, 7, 7, 7], [4], []):
        original = list(values)
        for _ in sort(values, True):
            pass
        assert values == original


def test_quick_sort_animates_partitioning_step_by_step():
    from algorithms import quick_sort

    steps = list(quick_sort(list(range(20, 0, -1)), True))

    assert len(steps) > 20  # one frame per comparison, not per partition
