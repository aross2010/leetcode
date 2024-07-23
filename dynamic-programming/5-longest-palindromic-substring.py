# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def longestPalindrome(s: str) -> str:

    # O(n^3) solution

    # max = ""
    # n = len(s)

    # if n <= 1:
    #     return s

    # for i in range(n):
    #     for j in range(n-1, i-1, -1):
    #         substring = s[i:j+1]
    #         rev = substring[::-1]
    #         if substring == rev and len(substring) > len(max):
    #             max = substring
    # return max



    #O(n^2) solution

    max = ""

    # odd cases
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome = s[left:right+1]
            if len(palindrome) > len(max):
                max = palindrome
            left -= 1
            right += 1
        

    # even cases
    for i in range(len(s)):
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindrome = s[left:right+1]
            if len(palindrome) > len(max):
                max = palindrome
            left-=1
            right+=1
    
    return max


print(longestPalindrome("babad"))