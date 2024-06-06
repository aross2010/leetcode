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
        
    print('here')

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