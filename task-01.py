import random
import time
from functools import lru_cache


def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])


def update_no_cache(array, index, value):
    array[index] = value


@lru_cache(maxsize=1000)
def cached_range_sum(array_id, L, R):
    return sum(array_id[L:R + 1])


def range_sum_with_cache(array, L, R):
    return cached_range_sum(tuple(array), L, R)


def update_with_cache(array, index, value):
    array[index] = value
    cached_range_sum.cache_clear()


N = 100_000
Q = 50_000
array = [random.randint(1, 100) for _ in range(N)]
queries = [
    ('Range', random.randint(0, N - 1), random.randint(0, N - 1)) if random.random() < 0.7
    else ('Update', random.randint(0, N - 1), random.randint(1, 100))
    for _ in range(Q)
]

start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        L, R = min(query[1], query[2]), max(query[1], query[2])
        range_sum_no_cache(array, L, R)
    elif query[0] == 'Update':
        update_no_cache(array, query[1], query[2])
no_cache_time = time.time() - start_time

start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        L, R = min(query[1], query[2]), max(query[1], query[2])
        range_sum_with_cache(array, L, R)
    elif query[0] == 'Update':
        update_with_cache(array, query[1], query[2])
cache_time = time.time() - start_time

print(f"Час виконання без кешування: {no_cache_time:.2f} секунд")
print(f"Час виконання з LRU-кешем: {cache_time:.2f} секунд")
