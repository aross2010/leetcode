/*

Given an integer array, nums, return an array, answer, such that answer[i] is equal to the product of all the elements of nums except nums[i]

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

You must write an algorithm that rund in O(n) time and without using the division operation

Example 1: 

    input: nums = [1, 2, 3, 4]
    output: [24, 12, 8, 6]

Example 2: 

    input: nums = [-1. 1, 0, -3, 3]
    output: [0, 0, 9, 0, 0]

Constraints: 

    - 2 <= nums.length <= 10^5
    - -30 <= nums[i] <= 30
    - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis)

*/

/*

APPROACH:

- loop through array twice 

- on first pass set result array to all the prefix values for the corresponding index in the nums array
    set indexed value in res to the prefix. after mulitply the corresponding el in nums array to the prefix and set that to the new prefix
 ** res is always lagging behind one element, therefore it will always get the product of all the numbers up until itself but not including

- on the second pass, loop backwards and multiply the prefix by the postfix and store in result array
    set indexed value in res to itself times the postfix (on first loop, postfix is 1 bc there are no elements to the right so its just the prefix)
    set postfix to the corresponding element in nums times itself

 ** looping through three times so n * 2 wich is time complexity O(n)
 ** if i were to take original brute force approach (loop through nums and then loop through it again calculating products, it would be time complexity O(n^2)

*/

const productExceptSelf = (nums: number[]): number[] => {
  const res = new Array(nums.length).fill(1)

  let prefix = 1
  for (let i = 0; i < nums.length; i++) {
    res[i] = prefix
    prefix *= nums[i]
  }

  let postfix = 1
  for (let i = nums.length - 1; i >= 0; i--) {
    res[i] *= postfix
    postfix *= nums[i]
  }

  return res
}

console.log(productExceptSelf([1, 2, 3, 4]))

/*

brute force approach O(n^2)

 for (let i = 0; i < nums.length; i++) {
     let prod = 1
     for (let j = 0; j < nums.length; j++) {
        if (j!== i) prod *= nums[j]
     }
     arr[i] = prod
 }

*/
