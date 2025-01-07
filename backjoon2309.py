inputNums = []
sum = 0
for _ in range(9):
    num = int(input())
    inputNums.append(num)
    sum += num
inputNums.sort()
diff = sum - 100
for i in range(0, 8, 1):
    k = diff - inputNums[i]
    if k in inputNums:
        inputNums.remove(inputNums[i])
        inputNums.remove(k)
        break
for j in range(7):
    print(inputNums[j])
