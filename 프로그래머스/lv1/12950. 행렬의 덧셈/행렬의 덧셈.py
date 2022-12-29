def solution(arr1, arr2):
    arr = arr1.copy()
    for x in range(len(arr1)) :
        for y in range(len(arr1[0])) :
            arr[x][y] += arr2[x][y]  
    return arr