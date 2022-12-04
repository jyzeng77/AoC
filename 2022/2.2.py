code_opp = {'rock': 'A', 'paper': 'B', 'scissors': 'C'}
code_self =  {'lose': 'X', 'draw': 'Y', 'win': 'Z'}

score = 0

# Rock = 1, Paper = 2, Scissors = 3; Lose = 0, Tie = 3, Win = 6

with open("p2.txt", mode='r') as f:
    strat_guide = [(line.split()) for line in f]
    for opponent, self in strat_guide:
        if self == code_self['draw']:
            score += 3
        elif self == code_self['win']:
            score += 6

        if opponent == code_opp['rock']:

            if self == code_self['lose']:
                # Play scissors
                score += 3
            if self == code_self['draw']:
                # Play rock
                score += 1
            if self == code_self['win']:
                # Play paper
                score += 2
            
        elif opponent == code_opp['paper']:

            if self == code_self['lose']:
                # Play rock
                score += 1
            if self == code_self['draw']:
                # Play paper
                score += 2
            if self == code_self['win']:
                # Play scissors
                score += 3
            
        elif opponent == code_opp['scissors']:

            if self == code_self['lose']:
                # Play paper
                score += 2
            if self == code_self['draw']:
                # Play scissors
                score += 3
            if self == code_self['win']:
                # Play rock
                score += 1
            

print(score)
