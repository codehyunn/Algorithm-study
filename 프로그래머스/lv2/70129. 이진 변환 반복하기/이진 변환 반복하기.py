def solution(s):
    iter_cnt, zero_cnt = 0,0
    while s != "1" :
        zero = s.count("0")
        zero_cnt += zero
        
        s = '1' * (len(s) - zero)
        c = len(s)

        s = ''
        while c > 0 :
            c, mod = divmod(c, 2)
            s += str(mod)
        s = s[::-1]
        iter_cnt += 1
        
    return [iter_cnt, zero_cnt]