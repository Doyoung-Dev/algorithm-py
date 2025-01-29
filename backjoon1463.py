from collections import deque
n = int(input())

def make(n):
    if n == 1:
        return 0
    q = deque([(n, 1)])
    while q:
        num = q.popleft()
        if num[0] % 3 == 0:
            if num[0] // 3 == 1:
                return num[1]
            q.append((num[0]//3, num[1]+1))
        if num[0] % 2 == 0:
            if num[0] // 2 == 1:
                return num[1]
            q.append((num[0]//2, num[1]+1))
        q.append((num[0]-1, num[1]+1))
        if num[0] - 1 == 0:
            return num[1]


print(make(n))
