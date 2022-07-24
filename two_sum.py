# Лекція 4 завдання 1
from typing import List


def two_sum(nums: List[int], target: int):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])
                return


two_sum([1, 2, 3], 4)
two_sum([2, 7, 11, 15], 9)
two_sum([3, 2, 4], 6)
two_sum([3, 3], 6)
