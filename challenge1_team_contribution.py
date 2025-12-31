def team_contribution(contributions): 
    length= len(contributions)
    impact=[1]*length # here we are doing [1]*length to create an array of 1s of size length
    for i in range(length):
        for j in range(length):
            if i!=j:
                impact[i]*=contributions[j]
    return impact
print(team_contribution([1,2,3,4]))  