"""Tests de performance — bloquent le merge si les seuils sont dépassés."""

import time
import pytest
from src.algorithms import (
    fibonacci,
    fibonacci_recursive,
    merge_sort,
    sieve_of_eratosthenes,
    matrix_multiply,
)


class TestPerformance:
    """Chaque test vérifie qu'un algorithme s'exécute sous un seuil de temps."""

    def _timed(self, func, *args, max_ms: float):
        start = time.perf_counter()
        result = func(*args)
        elapsed_ms = (time.perf_counter() - start) * 1000
        assert elapsed_ms < max_ms, (
            f"{func.__name__} took {elapsed_ms:.1f}ms, max allowed: {max_ms}ms"
        )
        return result

    def test_fibonacci_30_under_1ms(self):
        self._timed(fibonacci, 30, max_ms=1)

    def test_fibonacci_recursive_30_under_5ms(self):
        self._timed(fibonacci_recursive, 30, max_ms=5)

    def test_fibonacci_100_under_1ms(self):
        self._timed(fibonacci, 100, max_ms=1)

    def test_merge_sort_10k_under_100ms(self):
        import random
        arr = random.sample(range(100_000), 10_000)
        self._timed(merge_sort, arr, max_ms=100)

    def test_sieve_100k_under_100ms(self):
        self._timed(sieve_of_eratosthenes, 100_000, max_ms=100)

    def test_matrix_multiply_50x50_under_200ms(self):
        import random
        size = 50
        a = [[random.random() for _ in range(size)] for _ in range(size)]
        b = [[random.random() for _ in range(size)] for _ in range(size)]
        self._timed(matrix_multiply, a, b, max_ms=200)
