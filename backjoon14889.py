import itertools
N = int(input())
players = [i for i in range(1, N+1, 1)]
scores = [[0] * N] * N

for i in range(N):
    scores[i] = list(map(int, input().split()))

comb = list(itertools.combinations(players, int(N/2)))

min_diff = []
for j in range(len(comb)):
    team_link = players.copy()
    team_start = comb[j]
    for k in range(int(N/2)):
        team_link.remove(team_start[k])
    team_start_per = list(itertools.permutations(team_start, 2))
    team_link_per = list(itertools.permutations(team_link, 2))
    team_start_power = 0
    team_link_power = 0
    for p in range(len(team_start_per)):
        team_start_power += scores[(team_start_per[p][0])-1][(team_start_per[p][1])-1]
        team_link_power += scores[(team_link_per[p][0])-1][(team_link_per[p][1])-1]
    diff = abs(team_start_power-team_link_power)
    min_diff.append(diff)

print(min(min_diff))
