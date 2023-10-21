# https://www.codewars.com/kata/55983863da40caa2c900004e

from itertools import permutations


def next_bigger(n):
    num = str(n)
    result = {int(''.join(nums)) for nums in permutations(num, len(num))}
    result = sorted(list(result))
    try:
        print(result[result.index(n) + 1])
    except Exception:
        print(-1)

# def next_bigger(n):
#     nums = list(str(n))
#     for i in reversed(range(len(nums[:-1]))):
#         for j in reversed(range(i, len(nums))):
#             if nums[i] < nums[j]:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 nums[i + 1:] = sorted(nums[i + 1:])
#                 return int(''.join(nums))
#     return -1


next_bigger(513)
