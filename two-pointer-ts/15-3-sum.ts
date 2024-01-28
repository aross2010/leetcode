/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


APPROACH:

- sort the nums array (needed for two pointer method)

- initialize a 2d array

- loop through the nums array until the second to last element
    // avoid duplicates
    if (the last element in loop is the same as current) continue

        initialize j to be one element to the right of current
        initialize k to be the last element in nums

        while j is less than k
            caculate sum between element at i, j, & k

            if (sum is 0) found new triplet -> add to triplets array

             // avoid duplicates
             while (j < k and the element to the right of j equals j) push j to the right one element 
             while (j < k and the element to the left of k equals j) push k to the left one element 

                increment j and decremenet k

            else if sum < 0 incremenet j else decrement k
*/

const threeSum = (nums: number[]): number[][] => {
  nums.sort((a, b) => a - b)
  const triplets: number[][] = []

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue

    let j = i + 1,
      k = nums.length - 1

    while (j < k) {
      const sum = nums[i] + nums[j] + nums[k]
      if (sum === 0) {
        triplets.push([nums[i], nums[j], nums[k]])

        while (j < k && nums[j] === nums[j + 1]) j++
        while (j < k && nums[k] === nums[k - 1]) k--

        j++
        k--
      } else sum < 0 ? j++ : k--
    }
  }

  return triplets
}

const res = threeSum([-2, 0, 1, 1, 2])

console.log(res)
