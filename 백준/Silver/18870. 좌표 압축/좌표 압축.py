import sys 

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

value_dict = {num : i for i,num in enumerate(sorted(set(nums)))}

for i, num in enumerate(nums) :
    nums[i] = value_dict[num]

print(* nums)