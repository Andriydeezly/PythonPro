'''1. Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.'''
# List = map(int, input().split())
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
#         while right >= left:
#             mid = (left + right) // 2
#
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left

# Ділення націло
def last_value(n:int):
    last = n% 10
    return last

g =last_value(123)
print(g)