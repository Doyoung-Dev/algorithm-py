n = int(input())
nmap = [[0 for _ in range(n)] for _ in range(n)]
max_count = 0


def check_count():
    max_row_count = 0
    for i in range(n):
        row_count = 1
        for j in range(n - 1):
            if nmap[i][j] == nmap[i][j + 1]:
                row_count += 1
                if j == n-2:
                    max_row_count = max(row_count, max_row_count)
            else:
                max_row_count = max(row_count, max_row_count)
                row_count = 1
    max_col_count = 0
    for i in range(n):
        col_count = 1
        for j in range(n - 1):
            if nmap[j][i] == nmap[j + 1][i]:
                col_count += 1
                if j == n-2:
                    max_col_count = max(max_col_count, col_count)
            else:
                max_col_count = max(max_col_count, col_count)
                col_count = 1
    count = max(max_row_count, max_col_count)
    return count


for i in range(n):
    line = input()
    for j in range(n):
        nmap[i][j] = line[j]

# 가로 교환
for i in range(n - 1):
    for j in range(n):
        if nmap[j][i] != nmap[j][i + 1]:
            # 00 01 / 10 11 / 20 21
            old_a = nmap[j][i]
            old_b = nmap[j][i + 1]
            nmap[j][i] = old_b
            nmap[j][i + 1] = old_a
            now = check_count()
            max_count = max(now, max_count)
            nmap[j][i] = old_a
            nmap[j][i + 1] = old_b

# 세로 교환
for j in range(n):
    for i in range(n - 1):
        if nmap[i][j] != nmap[i + 1][j]:
            # 00 10 / 10 20 / 01 11
            old_a = nmap[i][j]
            old_b = nmap[i + 1][j]
            nmap[i][j] = old_b
            nmap[i + 1][j] = old_a
            now = check_count()
            max_count = max(now, max_count)
            nmap[i][j] = old_a
            nmap[i + 1][j] = old_b


print(max_count)
