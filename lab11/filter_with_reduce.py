from functools import reduce

def custom_filter(func, seq):
    return reduce(lambda acc, x: acc + [x] if func(x) else acc, seq, [])