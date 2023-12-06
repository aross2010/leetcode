// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

// approach -> compare the two strings and see if the contents are the same

const isAnagram = (s, t) => {
  if (s.length !== t.length) return false

  const counter = new Array(26).fill(0) // empty array w/ 26 elements
  for (let i = 0; i < s.length; i++) {
    counter[s.charCodeAt(i) - 97]++ // add count to the array index corresponding to the letter ascii code
    counter[t.charCodeAt(i) - 97]-- // subtract count from the array index corresponding to the letter ascii code
  }
  for (let i = 0; i < counter.length; i++) {
    if (counter[i] !== 0) return false // if there is more of one letter in one string than the other, return false
  }

  return true
}

console.log(isAnagram('aacc', 'ccac'))
