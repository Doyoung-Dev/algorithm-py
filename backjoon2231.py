inputNum = int(input())
num = int(inputNum/2)
while num <= inputNum:
    stringNum = str(num)
    numbers = list(stringNum)
    sum = 0
    for i in range(len(stringNum)):
        sum += int(stringNum[i])
    if (sum + num) == inputNum:
        print(num)
        break
    else:
        num += 1
if num > inputNum:
    print(0)
