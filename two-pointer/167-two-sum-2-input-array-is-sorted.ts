/*

Given a 1-indexed array of integers, numbers, that is already sorted in non-descreasing order, find two numbers such that they add upp to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length

Return that inidicies of the two numbers, index1, and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1: 

    input: numbers = [2, 7, 11, 15], target = 9
    output: [1,2]
    exaplanation: The sum of 2 and 7 is 9. Therefore index1 = (0+1) = 1, index2 = (1+1) = 2.

Example 2: 

    input: numbers = [2, 3, 4], target = 6
    output: [1, 3]
    explanation: The sum of 2 and 4 is 6. therefore index1 = (0+1) = 1, index2 = (2+1) = 3.

Example 3: 

    input: numbers = [-1, 0], target = -1
    output: [1,2]
    explanation: The sum of -1 and 0 is -1. Therefore index1 = (0+1) = 1, index2 = (1+1) = 2

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

*/

/*

APPROACH: 

since the array is sorted, this can be done in one pass of the array with two pointers
start on opposite ends of the array and have them join together towards the middle until target is reached.

- two pointers one at start of array, one at end

- loop until the low val + high val == target

    if low val + high val is greater than target, must move high val down to get closer to the taget value
    else move low val up to get closer to target value

- once loop ends, we have the target indicies, add 1 to each and return in an array

time: O(n)
space: O(1)

*/

const twoSum2 = (numbers: number[], target: number): number[] => {
  let low = 0,
    high = numbers.length - 1

  // if the two values sum equals target the loop ends and we have correct indicies
  while (numbers[low] + numbers[high] !== target) {
    if (numbers[low] + numbers[high] > target) high-- // move right pointer in
    else low++ // move left pointer in
  }

  return [low + 1, high + 1]
}

console.log(twoSum2([-1, 0], -1))

/*
brute force

const twoSum2 = (numbers: number[], target: number): number[] => {
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) return [i + 1, j + 1]
    }
  }

  return []
}

alt apporach to current

const twoSum = (numbers: number[], target: number): number[] => {
  let low = 0,
    high = numbers.length - 1

  while (low <= high) {
    if (numbers[low] + numbers[high] > target) high--
    else if (numbers[low] + numbers[high] < target) low++
    else return [low + 1, high + 1]
  }

  return []
}

*/
