def distribute_prizes(participants):
    participants = participants.copy()
    n = len(participants)
    for i in range(n-1):
        max_index = i
        for j in range(i+1,n):
            if participants[j][1] > participants[max_index][1]:
                max_index = j
        participants[i], participants[max_index] = participants[max_index], participants[i]
    return participants
players = [('Asha',88),('Ravi',95),('Meera',79),('Dev',95)]
ranking = distribute_prizes(players)
print("Ranking:")
for name,score in ranking:
    print(name,score)
ranking = distribute_prizes([('Asha',88),('Ravi',95),('Meera',79),('Dev',95)])
scores = [p[1] for p in ranking]
assert scores == sorted(scores, reverse=True)
assert ranking[0][1] == 95
print("All test cases passed!")
