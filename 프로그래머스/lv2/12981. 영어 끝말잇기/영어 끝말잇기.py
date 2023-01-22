def solution(n, words):
    used_words = []
    for idx, word in enumerate(words) :
        if word in used_words \
            or (len(used_words) > 0 and used_words[-1][-1] != word[0]) :
            return [idx%n+1,idx//n+1]
        else :
            used_words.append(word)
            
    return [0,0]