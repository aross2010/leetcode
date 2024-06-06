# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(self, s: str) -> int:
        
    sub = set()
    l = 0
    count = 0
    max = 0

    for r in range(len(s)):
        if s[r] not in sub:
            sub.add(s[r])
            count+=1
            if count > max:
                max = count
            continue

        # slide the window until valid substring
        while l <= r and s[l] != s[r]:
            sub.remove(s[l])
            l+= 1
                
        l+=1
        count = (r-l)+1


    return max