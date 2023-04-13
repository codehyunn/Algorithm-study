import re

def solution(files):
    change_file_list = []
    for idx, file in enumerate(files) :
        change_file = file.lower()
        no_num = re.compile('[^0-9]+')
        num = re.compile('[0-9]+')

        no_num_str = no_num.findall(change_file)
        head = no_num_str[0]
            
        number = int(num.findall(change_file)[0])
        change_file_list.append((idx, head, number))
        
    change_file_list.sort(key = lambda x : (x[1], x[2]))
    
    answer = []
    for idx, _, _ in change_file_list :
        answer.append(files[idx])
        
    return answer