n, s, m = map(int, input().split())

diff = list(map(int, input().split()))

current = set([s])  # 현재 가능한 볼륨을 저장하는 set

for d in diff:
    next_volumes = set()  # 다음 가능한 볼륨을 저장할 set

    for v in current:
        if 0 <= v + d <= m:
            next_volumes.add(v + d)
        if 0 <= v - d <= m:
            next_volumes.add(v - d)

    if not next_volumes:  # 다음 곡을 연주할 수 없으면 종료
        print(-1)
        exit()

    current = next_volumes  # 현재 볼륨을 업데이트

print(max(current))  # 가능한 최댓값 출력
