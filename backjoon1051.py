N, M = map(int, input().split())
mylist = [input() for _ in range(N)]


def cal_max(x, y):
    size = 0
    for i in range(x, N, 1):
        for j in range(y, M, 1):
            if mylist[x][y] == mylist[i][j] == mylist[x][j] == mylist[i][y] and (i-x) == (j-y):
                tmp = (j - y + 1) * (i - x + 1)
                size = max(size, tmp)
    return size


max_size = 0
for i in range(0, N, 1):
    for j in range(0, M, 1):
        max_size = max(max_size, cal_max(i, j))

print(max_size)
