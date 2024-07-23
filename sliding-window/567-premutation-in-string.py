# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

def checkInclusion(s1: str, s2: str) -> bool:

    dict1 = {}

    for i in range(len(s1)):
        prev = dict1.get(s1[i])
        if not prev:
            dict1.update({s1[i]: 1})
        else:
            dict1.update({s1[i]: prev+1})

    dict2 = {}
    n = len(s1)
    l = 0

    for r in range(len(s2)):
        prev = dict2.get(s2[r])
        if not prev:
            dict2.update({s2[r]: 1})
        else:
            dict2.update({s2[r]: prev+1})
        
        # once the window reaches the length of s1+1, shrink window to match length
        if r >= n:
            l = r-n
            # remove or decrement last element out of window
            removed = s2[l]
            prev_removed_count = dict2.get(removed)
            if prev_removed_count == 1:
                dict2.pop(removed)
            else:
                dict2.update({removed: prev_removed_count-1})
        
        # dict is now length of s1, check for equality
        if dict1 == dict2:
            return True

    return False


print(checkInclusion("adc", "dcda"))