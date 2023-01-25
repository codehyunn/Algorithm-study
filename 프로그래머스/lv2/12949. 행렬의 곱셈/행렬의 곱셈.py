from itertools import product

def solution(arr1, arr2):
    matrix, row = [],[]
    length = len(arr2[-1])
    
    for a,b in product(arr1,zip(*arr2)) :
        tmp = [x*y for x,y in zip(a,b)]
        row.append(sum(tmp))
        
        if len(row) == length :
            matrix.append(row)
            row = []
    
    return matrix
