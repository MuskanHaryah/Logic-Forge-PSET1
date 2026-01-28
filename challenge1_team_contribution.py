# def team_contribution(contributions): 
#     length= len(contributions)
#     impact=[1]*length 
#     for i in range(length):
#         for j in range(length):
#             if i!=j:
#                 impact[i]*=contributions[j]
#     return impact
# print(team_contribution([1,2,3,4]))    

# optimized version
def team_contribution(contributions): 
    length= len(contributions)
    prefix=[1]*length
    suffix=[1]*length
    impact=[1]*length 

    for i in range(1,length):
        prefix[i] = prefix[i-1] * contributions[i-1]
    for i in range(length-2,-1,-1):
        suffix[i] = suffix[i+1]* contributions[i+1]
    for i in range(length):
        impact[i] = prefix[i]*suffix[i]
        
    return impact
print(team_contribution([1,2,3,4]))  
print(team_contribution([-1, 1, 0, -3, 3]))  
