import itertools

h, w = map(int, input().split())
n = int(input())
stickers = list()
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    stickers.append((a, b))
comb = itertools.combinations(stickers, 2)

for (a1, b1), (a2, b2) in comb:
    candidates = [
        (a1, b1, a2, b2),
        (a1, b1, b2, a2),
        (b1, a1, a2, b2),
        (b1, a1, b2, a2)
    ]
    for f1, f2, s1, s2 in candidates:
        # 가로로 나란히 배치
        if f1 + s1 <= h and max(f2, s2) <= w:
            answer = max(answer, f1*f2 + s1*s2)
        # 세로로 나란히 배치
        if f2 + s2 <= w and max(f1, s1) <= h:
            answer = max(answer, f1*f2 + s1*s2)

print(answer)
