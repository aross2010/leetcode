# Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:

# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

# You should perform the cuts in order, you can change the order of the cuts as you wish.

# The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

# Return the minimum total cost of the cuts.

# Example 1:
# The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
# Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
    
# Example 2:

# Input: n = 9, cuts = [5,6,1,4,2]
# Output: 22
# Explanation: If you try the given cuts ordering the cost will be 25.
# There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.
 

# Constraints:

# 2 <= n <= 106
# 1 <= cuts.length <= min(n - 1, 100)
# 1 <= cuts[i] <= n - 1
# All the integers in cuts array are distinct.

# Input: n = 7, cuts = [1,3,4,5]
# Output: 16
# Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

def minCost(n: int, cuts: list[int]) -> int:
    map = dict()
    cuts.extend([n]) # add the end of stick to matrix
    cuts.insert(0, 0) # add the start of stick (0) to matrix
    cuts.sort() # make sure to sort in ascending order

    def calculateCell(left, right, cuts: list[int], map): 
        length = right-left # the length of the stick to cut
        min = 99999999
        for i in range(1, len(cuts)-1): # find the next cheapest cut based on available cut positions
            if cuts[i] < right and cuts[i] > left: # the cut position is in between the start and end of stick
                value = length + (map.get((left, cuts[i])) or 0) + (map.get((cuts[i], right)) or 0) # length of the stick plus the cost of cutting two sections of the stick that have already been calcuated as the cheapest cost of that section
                if value < min:
                    min = value
        return min # return the cheapest cuts option

    # traverse matrix bottom up
    for i in range(len(cuts) - 1, -1, -1):
        for j in range(len(cuts)):
            tuple = (cuts[i], cuts[j]) # cell position
            if i >= j-1:
                map.update({tuple: 0}) # fill lower diagonal half with zeros
            else:
                map.update({tuple: calculateCell(cuts[i], cuts[j], cuts, map)}) # calculate cell cost for upper diagonal half

    return map.get((0, n)) # return the top right cell in the matrix


def main(): 
    print(minCost(9, [5,6,1,4,2]))

main()