from typing import List


def search(nums: List[int], target: int) -> int:
    l, h = 0, len(nums) -1
    m = h // 2 # int division

    while target >= nums[l] and target <= nums[h]:

        if target == nums[l]:
            return l
        elif target == nums[h]:
            return h
        elif target == nums[m]:
            return m

        if target > nums[m]:
            l = m+1
        elif target < nums[m]:
            h = m-1
        
        m = (l+h) // 2
    
    return -1

print(search([-1,0,3,5,9,12], 2))