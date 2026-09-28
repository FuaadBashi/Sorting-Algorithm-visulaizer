"""Sorting algorithms as generators, so a UI can animate them one step at a time.

Each algorithm sorts `values` in place and yields a dict mapping list indices to a highlight role
("compare", "swap", "pivot" or "placed") after every step. The module has no pygame dependency,
so the algorithms are unit-tested directly.
"""

from collections.abc import Callable, Iterator

Step = dict[int, str]
Algorithm = Callable[[list[int], bool], Iterator[Step]]


def _in_order(a: int, b: int, ascending: bool) -> bool:
    """True if a may come before b."""
    return a <= b if ascending else a >= b


def bubble_sort(values: list[int], ascending: bool = True) -> Iterator[Step]:
    n = len(values)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            # The original swapped when num1 > num2 in *descending* mode, sorting backwards.
            if not _in_order(values[j], values[j + 1], ascending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
                yield {j: "swap", j + 1: "swap"}
            else:
                yield {j: "compare", j + 1: "compare"}
        if not swapped:
            return


def insertion_sort(values: list[int], ascending: bool = True) -> Iterator[Step]:
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and not _in_order(values[j], key, ascending):
            values[j + 1] = values[j]
            j -= 1
            yield {j + 1: "swap", i: "pivot"}
        values[j + 1] = key
        yield {j + 1: "placed"}


def selection_sort(values: list[int], ascending: bool = True) -> Iterator[Step]:
    n = len(values)
    for i in range(n):
        best = i
        for j in range(i + 1, n):
            if not _in_order(values[best], values[j], ascending):
                best = j
            yield {i: "pivot", j: "compare", best: "swap"}
        values[i], values[best] = values[best], values[i]
        yield {i: "placed"}


def merge_sort(values: list[int], ascending: bool = True) -> Iterator[Step]:
    def merge(start: int, mid: int, end: int) -> Iterator[Step]:
        left, right = values[start : mid + 1], values[mid + 1 : end + 1]
        i = j = 0
        for k in range(start, end + 1):
            if i < len(left) and (j >= len(right) or _in_order(left[i], right[j], ascending)):
                values[k] = left[i]
                i += 1
            else:
                values[k] = right[j]
                j += 1
            yield {k: "placed"}

    def sort(start: int, end: int) -> Iterator[Step]:
        if start >= end:
            return
        mid = (start + end) // 2
        yield from sort(start, mid)
        yield from sort(mid + 1, end)
        yield from merge(start, mid, end)

    yield from sort(0, len(values) - 1)


def quick_sort(values: list[int], ascending: bool = True) -> Iterator[Step]:
    def partition(start: int, end: int) -> Iterator[Step | int]:
        pivot = values[end]
        boundary = start
        for i in range(start, end):
            if _in_order(values[i], pivot, ascending):
                values[i], values[boundary] = values[boundary], values[i]
                boundary += 1
            # Yield every comparison: partition used to be a plain function, so a whole
            # partition happened within a single animation frame.
            yield {i: "compare", boundary: "swap", end: "pivot"}
        values[boundary], values[end] = values[end], values[boundary]
        yield {boundary: "placed"}
        yield boundary

    def sort(start: int, end: int) -> Iterator[Step]:
        if start >= end:
            return
        split = start
        for item in partition(start, end):
            if isinstance(item, int):
                split = item
            else:
                yield item
        yield from sort(start, split - 1)
        yield from sort(split + 1, end)

    yield from sort(0, len(values) - 1)


ALGORITHMS: dict[str, tuple[str, Algorithm]] = {
    "b": ("Bubble Sort", bubble_sort),
    "i": ("Insertion Sort", insertion_sort),
    "s": ("Selection Sort", selection_sort),
    "m": ("Merge Sort", merge_sort),
    "q": ("Quick Sort", quick_sort),
}
