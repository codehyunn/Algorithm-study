def solution(arr):
    for i in range(1,len(arr)) :
        a,b = (arr[i-1], arr[i]) if arr[i-1] < arr[i] else (arr[i], arr[i-1])
        while True :
            if b%a == 0 :
                arr[i] = arr[i-1]*arr[i]//a
                break
            else :
                a,b = b, a%b
                
    return arr[-1]