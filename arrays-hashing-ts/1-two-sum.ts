// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

const twoSum = (nums, target) => {
  const map = new Map<number, number>()

  for (let i = 0; i < nums.length; i++) {
    // ex. if map has key 9-7, (2), that means 2 + 7 = 9
    if (map.has(target - nums[i])) {
      return [map.get(target - nums[i]), i] // return [0, 1]
    } else {
      map.set(nums[i], i)
    }
  }
}

console.log(twoSum([2, 7, 11, 15], 9))
