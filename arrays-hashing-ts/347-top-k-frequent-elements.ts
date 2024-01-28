/*

Given an integer array, nums, and an integer, k, return the k most frequent elements. You may return the answer in any order.

Example 1: 

    input: nums = [1, 1, 1, 2, 2, 3], k = 2
    output: [1, 2]

Example 2: 

    input: nums = [1], k = 1
    output: [1]

Constraints: 

    - 1 <= nums.length <= 10^5
    - 10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of unique elements in the array].
    - It is guaranteed that the answer is unique

Follow up: Time complexity must be better than (n log n), where n is the array's size

*/

/*

APPROACH: 

- create a map with structure: 
{
    key: number,
    value: number
}

- loop through all nums

    if the map has a key with the number in it, add one to the count that is in the value
    else set a new entry with key being the number and an initial value being 1

- create an array from the map entries & sort in descending order by the values

- create empty array to use as return value

- loop from 0 to k (only pushing the first k keys from map)
    add the first element in each subarray (the key from the maps)

*/

const topKFrequent = (nums: number[], k: number): number[] => {
  const map = new Map()

  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i])) {
      const curr = map.get(nums[i]) + 1
      map.set(nums[i], curr)
    } else {
      map.set(nums[i], 1)
    }
  }

  const arr = Array.from(map.entries()).sort((a, b) => b[1] - a[1])
  const freqEl: number[] = []

  for (let i = 0; i < k; i++) {
    freqEl.push(arr[i][0])
  }

  return freqEl
}

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 1))
