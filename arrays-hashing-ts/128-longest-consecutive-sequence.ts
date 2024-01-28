/*

Given an unsorted array of integers, nums, return the length of the longest consecutive elements sequence

You must write an algorithm that runs in O(n) time

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9


*/

/*

APPROACH: 

- create a set that contains the nums array
- initialize a maximum length value, max, to 0

loops through the nums array 
    if the set contains the num - 1 then it is NOT the start of a sequence, move on to next num
    else it is the start of a sequence, in this case: 
        initialize a counter to 1 (this will record the length of the sequence)
        initialize the current num to a new variable
        keep adding 1 to current & counter as long as current is in the set (the set has all the nums values)
        compare counter to max to see which is higher, set higher to max

- return max

time complexity: 0(n) loop through the array once, use set for O(1) checking of if ++current exists in nums
space complexity: 0(n) creating a set that contains all of the elements in nums 

*/

const longestConsecutive = (nums: number[]): number => {
  const set = new Set(nums)
  let max = 0

  for (const num of nums) {
    if (set.has(num - 1)) continue // not the start of a sequence, continue to next element
    // start of a sequence
    let count = 1,
      current = num
    while (set.has(++current)) count++ //  while there is another element in sequential order add to count

    max = Math.max(count, max)
  }

  return max
}

console.log(longestConsecutive([100, 4, 200, 1, 3, 2]))
