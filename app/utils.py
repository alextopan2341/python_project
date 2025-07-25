from functools import lru_cache

def compute_pow(x: float, y: float) -> float:
    return x ** y

@lru_cache(maxsize=128)
def compute_fib(n: int) -> int:
    if n < 0:
        raise ValueError("n trebuie să fie >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@lru_cache(maxsize=128)
def compute_fact(n: int) -> int:
    if n < 0:
        raise ValueError("n trebuie să fie >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
