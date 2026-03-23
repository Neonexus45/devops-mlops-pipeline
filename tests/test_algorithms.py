"""Tests unitaires pour les algorithmes."""

import pytest
from src.algorithms import (
    fibonacci,
    fibonacci_recursive,
    bubble_sort,
    merge_sort,
    binary_search,
    is_prime,
    sieve_of_eratosthenes,
    matrix_multiply,
)

# ─── Fibonacci ───────────────────────────────────────────────────────


class TestFibonacci:
    def test_base_cases(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_known_values(self):
        assert fibonacci(10) == 55
        assert fibonacci(20) == 6765
        assert fibonacci(30) == 832040

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            fibonacci(-1)

    def test_recursive_matches_iterative(self):
        for n in range(25):
            assert fibonacci(n) == fibonacci_recursive(n)

    def test_large_value(self):
        result = fibonacci(50)
        assert result == 12586269025


# ─── Sorting ─────────────────────────────────────────────────────────


class TestSorting:
    @pytest.fixture
    def unsorted_list(self):
        return [64, 34, 25, 12, 22, 11, 90]

    @pytest.fixture
    def sorted_list(self):
        return [11, 12, 22, 25, 34, 64, 90]

    def test_bubble_sort(self, unsorted_list, sorted_list):
        assert bubble_sort(unsorted_list) == sorted_list

    def test_merge_sort(self, unsorted_list, sorted_list):
        assert merge_sort(unsorted_list) == sorted_list

    def test_empty_list(self):
        assert bubble_sort([]) == []
        assert merge_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([42]) == [42]
        assert merge_sort([42]) == [42]

    def test_already_sorted(self, sorted_list):
        assert bubble_sort(sorted_list) == sorted_list
        assert merge_sort(sorted_list) == sorted_list

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        assert bubble_sort(arr) == expected
        assert merge_sort(arr) == expected

    def test_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        expected = sorted(arr)
        assert bubble_sort(arr) == expected
        assert merge_sort(arr) == expected

    def test_does_not_mutate_input(self, unsorted_list):
        original = unsorted_list.copy()
        bubble_sort(unsorted_list)
        assert unsorted_list == original
        merge_sort(unsorted_list)
        assert unsorted_list == original


# ─── Binary Search ───────────────────────────────────────────────────


class TestBinarySearch:
    def test_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        assert binary_search(arr, 7) == 3

    def test_not_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        assert binary_search(arr, 4) == -1

    def test_first_element(self):
        assert binary_search([10, 20, 30], 10) == 0

    def test_last_element(self):
        assert binary_search([10, 20, 30], 30) == 2

    def test_empty_array(self):
        assert binary_search([], 5) == -1

    def test_single_element_found(self):
        assert binary_search([42], 42) == 0

    def test_single_element_not_found(self):
        assert binary_search([42], 99) == -1


# ─── Prime Numbers ───────────────────────────────────────────────────


class TestPrimes:
    def test_small_primes(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True

    def test_non_primes(self):
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(4) is False
        assert is_prime(9) is False
        assert is_prime(100) is False

    def test_large_prime(self):
        assert is_prime(104729) is True

    def test_sieve_small(self):
        assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

    def test_sieve_edge(self):
        assert sieve_of_eratosthenes(1) == []
        assert sieve_of_eratosthenes(2) == [2]

    def test_sieve_count(self):
        primes = sieve_of_eratosthenes(100)
        assert len(primes) == 25


# ─── Matrix Multiplication ──────────────────────────────────────────


class TestMatrixMultiply:
    def test_identity(self):
        a = [[1, 0], [0, 1]]
        b = [[5, 6], [7, 8]]
        assert matrix_multiply(a, b) == b

    def test_basic(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        assert matrix_multiply(a, b) == [[19, 22], [43, 50]]

    def test_non_square(self):
        a = [[1, 2, 3]]
        b = [[4], [5], [6]]
        assert matrix_multiply(a, b) == [[32]]

    def test_incompatible_raises(self):
        a = [[1, 2]]
        b = [[3, 4]]
        with pytest.raises(ValueError):
            matrix_multiply(a, b)
