def solution(babbling):
    words = ['aya', 'ye', 'ma', 'woo']
    two_words = ['woowoo', 'ayaaya', 'yeye', 'mama']
    
    for i in range(len(babbling)) :
        for tword in two_words :
            if tword in babbling[i] :
                break
        else :
            for word in words :
                if word in babbling[i] :
                    babbling[i] = babbling[i].replace(word, " ")
            babbling[i] = babbling[i].strip()
            
    answer = babbling.count('')
    return answer