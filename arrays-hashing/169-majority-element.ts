/*

Given an array, nums of size n, return the majority element

The majority element is the element that appears more than [n/2] times. You may assume that the majority element always exists in the array

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

*/

/*

APPROACH: ** Can only use this algorithm if we are sure that a majority element exists, which is said in the description

-initialize majorityEl and count to be zero

- loop through all nums 
    if count is zero, meaning there is no current majority, set majority El to num
    ** if num was a majority element, then it would not have been canceled out by the other minor elements

    if num === majorityEl, add one to count else subtract one

return the majority El

o(n) time only one loop
o(1) space only creating variables for count and majorityEl

*/

const majorityElement = (nums: number[]): number => {
  // boyer-moore majority vote algo must be an element that appears greater than n/2 times

  let majorityEl = 0
  let count = 0

  for (const num of nums) {
    if (count === 0) {
      majorityEl = num
    }

    count += num === majorityEl ? 1 : -1
  }

  return majorityEl
}

console.log(majorityElement([3, 2, 3]))

// could also use hash map solution and return the key from the greatest value -- slower and more space used

// const majorityElement = (nums: number[]): number => {
//     const map = new Map<number, number>()

//     for (const num of nums) {
//       const current = map.get(num)
//       if (current) map.set(num, current + 1)
//       else map.set(num, 1)
//     }

//     const arr = Array.from(map.entries()).sort((a, b) => b[1] - a[1])

//     return arr[0][0]
//   }
