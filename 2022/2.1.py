code_opp = {'rock': 'A', 'paper': 'B', 'scissors': 'C'}
code_self =  {'rock': 'X', 'paper': 'Y', 'scissors': 'Z'}

score = 0

with open("p2.txt", mode='r') as f:
    strat_guide = [(line.split()) for line in f]
    for opponent, self in strat_guide:
        if self == code_self['rock']:
            score += 1
            if opponent == code_opp['rock']:
                score += 3
            if opponent == code_opp['scissors']:
                score += 6
        elif self == code_self['paper']:
            score += 2
            if opponent == code_opp['paper']:
                score += 3
            if opponent == code_opp['rock']:
                score += 6
        elif self == code_self['scissors']:
            score += 3 
            if opponent == code_opp['scissors']:
                score += 3
            if opponent == code_opp['paper']:
                score += 6

print(score)
