def solution(board, moves):
    board = [[0]*len(board)]+[list(x) for x in zip(*board)]
    basket = []
    answer = 0
    
    for m in moves :
        for i,n in enumerate(board[m]) :
            if n != 0 :
                board[m][i] = 0
                if basket and n == basket[-1] :
                    basket.pop()
                    answer += 2
                else :
                    basket.append(n)
                break
    return answer