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