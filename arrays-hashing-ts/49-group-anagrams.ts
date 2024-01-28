// Given an array of strings strs, group the anagrams together. You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
// Example 2:

// Input: strs = [""]
// Output: [[""]]
// Example 3:

// Input: strs = ["a"]
// Output: [["a"]]

// Constraints:

// 1 <= strs.length <= 104
// 0 <= strs[i].length <= 100
// strs[i] consists of lowercase English letters.

/*

APPROACH:

- create a map with structure as such: 
{
    key: sorted string (need to sort so all anagrams are equal)
    value: array of the original string (unsorted)
}

- loop through all strings:

    1. sort the string then check: 

        if the map has a key matching the sorted string, push the original string onto its value array
        else create a new entry with the key being the sorted string and the value being an array of just the original string


- return as an array of all the values in the map
        
*/

const groupAnagrams = (strs: string[]): string[][] => {
  const map = new Map()

  for (let i = 0; i < strs.length; i++) {
    let str = strs[i].split('').sort().join('')

    if (map.has(str)) {
      map.get(str).push(strs[i])
    } else {
      map.set(str, [strs[i]])
    }
  }

  return Array.from(map.values())
}

console.log(groupAnagrams(['a']))
