/*

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

*/

/*

APPROACH: 

- convert the string to filter out the non-alphanumeric charcters and convert to lowercase

- use two pointers one on each end of the string and compare the characters bringing them closer together

*/

const isPalindrome = (s: String): boolean => {
  const str = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase() // remove all non-alphanumeric characters, then convert to lower case

  // use two pointers to see if opposite end chars equal the other
  for (let i = 0, j = str.length - 1; i < j; i++, j--) {
    if (str[i] != str[j]) return false
  }

  return true
}

console.log(isPalindrome(' '))
