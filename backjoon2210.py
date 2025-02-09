board = [[0] * 5] * 5
for a in range(5):
    board[a] = list(map(int, input().split()))

num_list = set()


def run(i, j, depth, num):
    if depth < 5:
        # 상 (i-1, j)
        if 0 <= i - 1 <= 4:
            run(i - 1, j, depth + 1, str(num)+str(board[i-1][j]))
        # 하 (i+1, j)
        if 0 <= i + 1 <= 4:
            run(i + 1, j, depth + 1, str(num)+str(board[i+1][j]))
        # 좌 (i, j-1)
        if 0 <= j - 1 <= 4:
            run(i, j - 1, depth + 1, str(num)+str(board[i][j-1]))
        # 우 (i, j+1)
        if 0 <= j + 1 <= 4:
            run(i, j + 1, depth + 1, str(num)+str(board[i][j+1]))
    else:
        num_list.add(num)
        return


for i in range(5):
    for j in range(5):
        start = board[i][j]
        run(i, j, 0, start)

print(len(num_list))
