from typing import List


def minCost(n: int, cuts: List[int]) -> int:
    map = dict()
    cuts.extend([n]) # add the end of stick to matrix
    cuts.insert(0, 0) # add the start of stick (0) to matrix
    cuts.sort() # make sure to sort in ascending order

    def calculateCell(left, right, cuts: List[int], map): 
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