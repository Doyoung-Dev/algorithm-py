import itertools

n, s = map(int, input().split())

nums = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    comb = itertools.combinations(nums, i)
    for c in comb:
        if sum(c) == s:
            count += 1

print(count)
