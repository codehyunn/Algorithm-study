def solution(n, words):
    answer = [0,0]
    used_words = []
    for idx, word in enumerate(words) :
        if word in used_words \
            or (len(used_words) > 0 and used_words[-1][-1] != word[0]) :
            answer = [idx%n+1,idx//n+1]
            break
        else :
            used_words.append(word)
            
    return answer