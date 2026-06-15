"""Collection d'algorithmes Python — support pour le pipeline CI/CD."""


def fibonacci(n: int) -> int:
    """Calcule le n-ième nombre de Fibonacci (itératif)."""
    if n < 0:
        raise ValueError("n must be non-negatives")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n: int) -> int:
    """Calcule le n-ième nombre de Fibonacci (récursif avec mémoïsation)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    memo = {}

    def _fib(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            return k
        memo[k] = _fib(k - 1) + _fib(k - 2)
        return memo[k]

    return _fib(n)


def bubble_sort(arr: list) -> list:
    """Tri à bulles."""
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def merge_sort(arr: list) -> list:
    """Tri fusion."""
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search(arr: list, target) -> int:
    """Recherche binaire. Retourne l'index ou -1."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def is_prime(n: int) -> bool:
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Crible d'Ératosthène — retourne tous les nombres premiers jusqu'à limit."""
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i, v in enumerate(is_p) if v]


def matrix_multiply(a: list[list], b: list[list]) -> list[list]:
    """Multiplication de matrices."""
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    rows_a, cols_b, cols_a = len(a), len(b[0]), len(a[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result
