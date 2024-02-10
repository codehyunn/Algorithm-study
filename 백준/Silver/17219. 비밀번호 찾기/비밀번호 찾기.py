import sys  
input = sys.stdin.readline

n,m = map(int,input().split())

pwd_dict = dict()
for _ in range(n) :
    address, pwd = input().split()
    pwd_dict[address] = pwd 
    
for _ in range(m) :
    x = input().rstrip()
    print(pwd_dict[x])