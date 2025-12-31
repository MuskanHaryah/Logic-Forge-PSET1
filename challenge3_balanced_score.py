def balanced_median(scoresA, scoresB):
    m, n = len(scoresA), len(scoresB)
    total = m + n
    mid = total// 2
    
    i = j = 0
    prev = cur = 0
    
    for _ in range(mid + 1):
        prev = cur
        
        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            cur = scoresA[i]
            i += 1
        else:
            cur = scoresB[j]
            j += 1
    
    if total % 2 == 1:
        return float(cur)
    return (prev + cur) / 2.0

print(balanced_median([1,3], [2]))        
print(balanced_median([1,2], [3,4]))      
