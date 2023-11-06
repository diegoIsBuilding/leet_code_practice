#Problem 1: Two Sum
#Given the array of integers 'nums' and an integer 'target'
#return indicies of the two numbers such that they add up
#to the target

#Assume: each input has exactly one solution and you may 
#not use the same element twice

#Example: 
#Input = [2, 7, 11, 15], target = 9
#Output = [0, 1]
#Explanation Because num[0] which is equal to 2 plus num[1] 
#which is equal to 7 and by adding the value of each indicies
#you get the value of the target which is 9

#Approach: One-Pass Hash Table
#The idea of this approach is to scan the list of numbers 'nums'
#exactly once

#As you scan the list of numbers - you calculate what you need to 
#add to the current number to reach the 'target' sum

#You use a hash table (data structure) to rememeber the numbers
#you have already 'seen'/'scanned' - along with their indicies in the array

#If you find the complement of the current number in the hash table
#it means you have found the two numbers that add up to the 'target' sum
#return their indicies immediately 
from pyparsing import List


class Solution:
    #'nums' is a list of integers, 'target' is a single integer
    #The method returns a list of intergers(these are the indicies 
    #of the nums that add up to the target)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap is an empty dictionary
        #dictionaries are collections of key: value pairs
        #used to implement hash tables
        hashmap = {}
        #this line starts a loop that goes through each index 'i'
        #of the 'num' list
        for i in range(len(nums)):
            #in the loop:
            #for each number in the 'nums' list we calculate
            #the complement by subtracting the current number
            #from the 'target'
            complement = target - nums[i]
            #check if the complement of the current number already 
            #exists as a key in our 'hashmap'
            if complement in hashmap:
                #if the complement is found in the hashmap then it means
                #the current number and number at the index of the complement 
                #in hashmap add up tp the target value
                #So we return indices in a list 
                return [i, hashmap[complement]]
            #if the complement is not found, we add the current number and its index
            #to the hashmap and contiue the loop
            hashmap[nums[i]] = i
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # This would output: [0, 1] because nums[0] + nums[1] == 9

#================================================================================
#Two-pass Hash Table Approach: 
#Algorithm Exlplanation

# 1) In the first pass through the array. we put each element and its index into 
#a hash table

# 2) In the second pass we look for each elements complement in the hash table
# If we find it we have our solution: The index of the current element
# and its complement 

# 3) We need to ensure that we dont use the same element twice: the complement
# must be a different element 

#Time complexity Analysis:
#The alogrithm has a time complexity of O(n): We go through the list of n elements
#Twice: once to build the hash table and once to find the complement 
#Because hash tables lookups are O(1) on average the over time complexity is O(n)

#Space complexity: is O(n) we need a hash table that stores each of the n elements

class Solution2: 
    #nums accepts a list of integers and target accepts an integer value
    #finally the funtion returns a list of integers
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #First we create an empty dictionary(works as our hashmap)
        hashmap = {}
        #Next we are going to loop through list of integers in the 'nums' list
        #storing each number as a key and its index ex: [0, 73] first value pair - 
        #these values will be stored in the hashmap
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            #In the second pass - we calculate what we need to add to each number to reach the target
            #this the result of this calculation is the complement
            for i in range(len(nums)):
                complement = target - nums[i]
                #We then check if the complement value is in the hash table and also make sure
                #that it is not the same element we are looking at (we can use the same element twice)
                if complement in hashmap and hashmap[complement] != i:
                    #if the complement exists and it is different than the 
                    #current element then we return a list containing the index values that add up to the target
                    #basically these values are the current index and the index of the complemenet 
                    return [i, hashmap[complement]]
                
solution2 = Solution2()
result2 = solution2.twoSum([2, 7, 11, 15], 9)
print(result2)

