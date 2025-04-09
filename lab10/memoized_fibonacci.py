import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

# Standard recursive Fibonacci (slow)
def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)

# Memoized recursive Fibonacci (fast)
@memoize
def recur_fibo_memo(n):
    if n <= 1:
        return n
    return recur_fibo_memo(n - 1) + recur_fibo_memo(n - 2)

def main():
    n = 35

    print(f"Calculating recur_fibo({n}) without memoization...")
    start = time.time()
    result = recur_fibo(n)
    print("Result:", result)
    print("Time (non-memoized):", time.time() - start, "seconds\n")

    print(f"Calculating recur_fibo({n}) with memoization...")
    start = time.time()
    result = recur_fibo_memo(n)
    print("Result:", result)
    print("Time (memoized):", time.time() - start, "seconds")

if __name__ == "__main__":
    main()
