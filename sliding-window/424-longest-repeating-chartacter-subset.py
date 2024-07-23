# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

def characterReplacement( s: str, k: int) -> int:
    l = res = max_freq = 0
    counter = {}
    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1
        max_freq = max(max_freq, counter[s[r]])
        len_window = r-l+1
        # if not possible to make valid substring, shift window start of window
        if len_window - max_freq > k:
            counter[s[l]] -= 1
            l += 1
            len_window -= 1
        res = max(res, len_window)
    return res

print(characterReplacement("ABAB", 2)) # 4