def solution(board, moves):
    board = [[0]*len(board)]+[list(x) for x in zip(*board)]
    basket = []
    answer = 0
    
    for m in moves :
        idx, x = len(board), -1
        for i,n in enumerate(board[m]) :
            if n != 0 :
                idx, x = i, n
                board[m][i] = 0
                break
        else :
            continue
        
        if basket and x == basket[-1] :
            basket.pop()
            answer += 2
        else :
            basket.append(x)
            
    return answer