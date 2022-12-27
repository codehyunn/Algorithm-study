strs = input('')
result = ['']
tmp = ''

for i,s in enumerate(strs) :
    if s not in ['-', '+'] :
        tmp += s

    else :
        result[-1] += str(int(tmp))
        tmp = ''

        if s == '-':
            result.append('')
        else :
            result[-1] += s

result[-1] += str(int(tmp))

eval_result = list(map(eval, result))
str_result = list(map(str,eval_result))
final_result = '-'.join(str_result)
ans = eval(final_result)
print(ans)