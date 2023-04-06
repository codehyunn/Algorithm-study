def solution(dirs) : 
    visited_pairs = []
    move_dict = {'R':0, 'L':1, 'U':2, "D":3}
    dx, dy  = [0,0,1,-1], [1,-1,0,0]

    count = 0
    prev_x, prev_y = 0,0

    for d in dirs :
        idx = move_dict[d]
        x,y = prev_x+dx[idx], prev_y+dy[idx]

        if -5 <= x <= 5 and -5<=y<=5 :
            if prev_x < x or prev_y < y: 
                pair = (prev_x, prev_y, x, y)
            else :
                pair = (x,y,prev_x,prev_y)
            
            if pair not in visited_pairs :
                count += 1
                visited_pairs.append(pair)

            prev_x, prev_y = x,y

    return count