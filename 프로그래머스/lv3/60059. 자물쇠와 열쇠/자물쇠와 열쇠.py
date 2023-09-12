def rotation(m, key_outs) :
    rotated_key = []
    
    if m % 2 == 0 :
        center = (m-1)/2
    else :
        center = m//2
        
    for (x,y) in key_outs :
        sx, sy = y, int((-1*(x-center))+center)
        rotated_key.append((sx,sy))
        
    return rotated_key
    
def solution(key, lock):
    m, n = len(key), len(lock) 
    key_outs = []
    for i in range(m) :
        for j in range(m) :
            if key[i][j] == 1 :
                key_outs.append((i,j))
    
    if not key_outs :
        return False
    
    lock_homes = []
    for i in range(n) :
        for j in range(n) :
            if lock[i][j] == 0 :
                lock_homes.append((i,j))
    
    if len(lock_homes) > len(key_outs) :
        return False
    
    for _ in range(4) :
        for i in range(-(m-1), n+1) :
            for j in range(-(m-1), n+1) :
                count = 0
                for (x,y) in key_outs :
                    sx, sy = x+i, y+j
                    if 0<=sx<n and 0<=sy<n :
                        if (sx,sy) in lock_homes :
                            count += 1
                        else :
                            break
                            
                if count == len(lock_homes) :
                    return True
                
        key_outs = rotation(m, key_outs)
                     
    return False