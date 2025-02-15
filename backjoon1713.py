n = int(input())
num = int(input())
candidates = list(map(int, input().split()))
votes = [0] * 101
dq = list()


def find():
    min_idx = float('inf')
    min_votes = float('inf')
    mins = list()
    for idx in range(n):
        d = dq[idx]
        if min_votes > votes[d]:
            min_votes = min(votes[d], min_votes)
            mins.clear()
            mins.append(idx)
            min_idx = idx
        elif min_votes == votes[d]:  # 동일한 투표 개수
            mins.append(idx)
        else:
            continue
    if len(mins) > 1:
        mins.sort()
        return mins[0]
    else:
        return min_idx


for i in range(num):
    if candidates[i] in dq:
        votes[candidates[i]] += 1
    else:
        if len(dq) >= n:
            toDelIdx = find()
            toDel = dq[toDelIdx]
            dq.remove(toDel)
            votes[toDel] = 0
        dq.append(candidates[i])
        votes[candidates[i]] += 1

dq.sort()
for l in dq:
    print(l, end=" ")
