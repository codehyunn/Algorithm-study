from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_counter = defaultdict(list)
    play_counter = defaultdict(int)
    
    for idx, genre in enumerate(genres) :
        genre_counter[genre].append((idx, plays[idx]))
        play_counter[genre] += plays[idx]
        
    play_counter = sorted(play_counter.items(), key=lambda x:x[1], reverse = True)
    for key, _ in play_counter :
        genre_counter[key].sort(key=lambda x:(x[1], -x[0]), reverse = True)
        answer.append(genre_counter[key][0][0])
        if len(genre_counter[key]) >= 2 : answer.append(genre_counter[key][1][0])

    return answer