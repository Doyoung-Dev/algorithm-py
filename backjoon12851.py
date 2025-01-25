from collections import deque

N, K = map(int, input().split())

def answer(n, k):
    check = [-1] * 100001

    nums = deque([(n, 0)])

    check[n] = 0
    count = 0

    while nums:
        num, t = nums.popleft()

        if num == k:
            if check[k] == -1:
                check[k] = t
                count = 1
            elif check[k] == t:
                count += 1
            continue

        for next_num in (num + 1, num - 1, 2 * num):
            if 0 <= next_num <= 100000:
                if check[next_num] == -1 or check[next_num] == t + 1:
                    check[next_num] = t + 1
                    nums.append((next_num, t + 1))
    return check[k], count


tm, ct = answer(N, K)
print(tm)
print(ct)
