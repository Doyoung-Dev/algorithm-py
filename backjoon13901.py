r, c = map(int, input().split())
room = [[0 for _ in range(c)] for _ in range(r)]
k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    room[br][bc] += 1
sr, sc = map(int, input().split())
room[sr][sc] = 1 # 첫 위치 방문 표시
seq = list(map(int, input().split()))
direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)] # [0]은 안쓰는 값, 상하좌우
flag = True
idx = 0
count = 0

while flag:
    seq_now = seq[idx]
    now = direction[seq_now]
    i, j = now[0], now[1]
    if sr+i < 0 or sr+i >= r or sc+j < 0 or sc+j >= c or room[sr+i][sc+j] == 1 : # 다음을 못가는 경우
        idx += 1  # 다음 순서로 넘김
        idx %= len(seq)
        count += 1
        if count == 5:
            flag = False
    else: # 다음을 갈 수 있는 경우
        sr = sr+i
        sc = sc+j
        room[sr][sc] = 1
        count = 0
print(sr, sc)
