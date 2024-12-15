from dataclasses import dataclass


@dataclass
class Team:
    name: str
    members: list
    contest_id: int
    rank: int


n, m, t, k = map(int, input().split())

cons = [[] for _ in range(m + 1)]
for _ in range(n):
    team_info = input().split()
    team = Team(
        name=team_info[0],
        members=team_info[1:4],
        contest_id=int(team_info[4]),
        rank=int(team_info[5]),
    )
    cons[team.contest_id].append(team)

all_teams = []
for contest_id in range(1, m + 1):
    all_teams.extend(cons[contest_id])
all_teams.sort(key=lambda x: (x.rank, x.contest_id))

adv_team = []
adv_men = set()

for team in all_teams:
    if len(adv_team) >= k:
        break
    
    if not any(member in adv_men for member in team.members):
        adv_team.append(team)
        adv_men.update(team.members)

print(len(adv_team))
for team in adv_team:
    print(team.name, *team.members)
