def solution(nums):
    answer = 0
    num_list = set(nums)
    if len(num_list) > len(nums)//2:
        return len(nums)//2
    else:
        return len(num_list)