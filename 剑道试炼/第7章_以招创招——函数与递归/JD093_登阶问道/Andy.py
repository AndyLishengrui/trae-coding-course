from functools import lru_cache
@lru_cache(None)
def f(n):return n if n<=2 else f(n-1)+f(n-2)
n=int(input());print(f(n))
