ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]


scores = { } 
score = 0 



for ballot in ballots: 
    for medal, name in ballot.items():  
        if medal == 'gold':  
            score += 3
            if name not in scores: 
                scores[name] = score
        if 'silver' in medal: 
            score += 2 
            if name not in scores: 
                scores[name] = score
        if 'broze' in medal:  
            score += 1 
            if name not in scores: 
                scores[name] = score

print(scores) 
            

# for key, value in scores.items(): 
#     print(key) 
#     print(value) 

            

print(scores)


