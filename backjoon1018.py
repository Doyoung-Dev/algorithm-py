def min_paint_cost(N, M, board):
    chess_board_W = [[("W" if (i+j) % 2 == 0 else "B") for j in range(8)] for i in range(8)]
    chess_board_B = [[("B" if (i + j) % 2 == 0 else "W") for j in range(8)] for i in range(8)]

    def calc_paint_cost(x, y):
        cost_W = 0
        cost_B = 0
        for i in range(8):
            for j in range(8):
                if board[x+i][y+j] != chess_board_W[i][j]:
                    cost_W += 1
                if board[x+i][y+j] != chess_board_B[i][j]:
                    cost_B += 1
        return min(cost_W, cost_B)

    min_cost = float('inf')
    for i in range(N-7):
        for j in range(M-7):
            min_cost = min(min_cost, calc_paint_cost(i, j))

    return min_cost

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    print(min_paint_cost(N, M, board))



# Try
#
# inputs = input().split()
# n = int(inputs[0])
# m = int(inputs[1])
# myboard = list()
# min = n*m
#
# count1 = 0
# count2 = 0
#
# case1 = "BWBWBWBW"
# case2 = "WBWBWBWB"
#
# # 입력
# for i in range(n):
#     myboard.append(list(input()))
#
# # 비교
# for i in range(0, n-8+1, 1):
#     for j in range(0, m-8+1, 1):
#         print("")
#         for k in range(8):
#             for l in range(8):
#                 if myboard[i+k][j+l] == case1[k]

