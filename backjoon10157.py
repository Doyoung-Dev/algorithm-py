c, r = map(int, input().split())
k = int(input())

arr = list()
curr = (1, 0)

curr_r = r
curr_c = c - 1

r_flag = True
c_flag = True

while curr_r >= 0 and curr_c >= 0:
    for _ in range(1, curr_r + 1):
        if r_flag:
            curr = (curr[0], curr[1] + 1)
        else:
            curr = (curr[0], curr[1] - 1)
        arr.append(curr)

    for _ in range(1, curr_c + 1):
        if c_flag:
            curr = (curr[0] + 1, curr[1])
        else:
            curr = (curr[0] - 1, curr[1])
        arr.append(curr)
    r_flag = not r_flag
    c_flag = not c_flag
    curr_r -= 1
    curr_c -= 1

if k > c*r:
    print(0)
elif k < 1:
    print(0)
else:
    print(arr[k-1][0], arr[k-1][1])
