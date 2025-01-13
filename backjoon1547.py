# 1. 입력 받기
M = int(input())

# 2. 컵 리스트 생성 [0, 1, 2, 3]
cups = [i for i in range(4)]

# 3. M번의 for 문 반복
for _ in range(M):
    X, Y = map(int, input().split())
    x = cups.index(X)
    y = cups.index(Y)
    tmp = cups[x]
    cups[x] = cups[y]
    cups[y] = tmp

# 4. 공이 들어 있는 컵의 번호 출력
print(cups[1])
