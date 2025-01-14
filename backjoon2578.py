# input: chulsoo_board, calls
# initialize bingo_board
chulsoo_board = [[0 for _ in range(5)] for _ in range(5)]
bingo_board = [[0 for _ in range(5)] for _ in range(5)]
calls = list()
for i in range(5):
    chulsoo_board[i] = list(map(int, input().split()))

for _ in range(5):
    inputs = input().split()
    for i in range(5):
        calls.append(int(inputs[i]))
calls.reverse()


def bingo_count():
    bingoCount = 0
    # 가로줄 빙고
    for i in range(5):
        lineSum = 0
        for j in range(5):
            lineSum += bingo_board[i][j]
            if lineSum == 5: bingoCount += 1
    # 세로줄 빙고
    for i in range(5):
        lineSum = 0
        for j in range(5):
            lineSum += bingo_board[j][i]
            if lineSum == 5: bingoCount += 1
    if bingo_board[0][0] + bingo_board[1][1] + bingo_board[2][2] + bingo_board[3][3] + bingo_board[4][4] == 5:
        bingoCount += 1
    if bingo_board[0][4] + bingo_board[1][3] + bingo_board[2][2] + bingo_board[3][1] + bingo_board[4][0] == 5:
        bingoCount += 1
    return bingoCount


def check():
    # calls 돌면서 chulsoo_board 비교하고, 동일하면 bingo_board 1로 업데이트
    count = 0
    for index in range(25):
        target = calls.pop()
        for x in range(5):
            for y in range(5):
                if chulsoo_board[x][y] == target:
                    bingo_board[x][y] = 1
                    count += 1
                    # 12개 이후부터 빙고 카운트
                    if count >= 12:
                        if bingo_count() >= 3:
                            print(index+1)
                            return


check()
