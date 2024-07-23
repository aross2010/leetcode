# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        # edge cases
        if n > m:
            return ""
        
        if s == t:
            return t
    
        # intial map of t
        t_map = {}
        for i in range(n):
            char_key = t_map.get(t[i])
            if char_key:
                t_map.update({t[i]: char_key+1})
            else:
                t_map.update({t[i]: 1})

        need = len(t_map.keys())
        have = 0

        window_map = {key: 0 for key in t_map}
        min_len = 1000000
        min_indices = None
        l = 0
        for r in range(m):
            valid_char = t_map.get(s[r])
            if not valid_char:
                continue
        
            updated_count = window_map.get(s[r]) + 1
            window_map.update({s[r]: updated_count})

            # the single char meets requirements
            if updated_count == t_map.get(s[r]):
                have += 1

            # valid window - all character count requirements met
            while have >= need:
                len_substring = r-l+1
                if len_substring < min_len:
                    min_len = len_substring
                    min_indices = (l, r)
            
                valid_char = t_map.get(s[l])
                if valid_char:
                    updated_count = window_map.get(s[l]) - 1
                    window_map.update({s[l]: updated_count})
                    if updated_count < t_map.get(s[l]):
                        have -= 1
                l+=1
    
        if not min_indices: return ""
        else: return s[min_indices[0]:min_indices[1]+1]

print(minWindow("ADOBECODEBANC", "ABC"))  



