#Concept
#When you  add numbers starting from the least significant digit (the right most digit)
#you sometimes get a sum that is 10 or greater, requiring you to carry the "excess" to 
#the next significant digit - In a linked list representing a number in reverse order
#this is like adding the values of corresponding nodes, keeping track of the carry and
#moving on to the next nodes

#Approach
#1) Start with a dummy node: The dummy node simplifies the code because you
# dont need to write seperate logic for the head of the result list

#Initialize Variables
#2) 'carry': This is set to zero because depending on the sum of two ditits 
#any previous carry exceeds 9

#3) 'current': This is a pointer to construct the result linked list
#starting from the dummy head

#Iterate over both Lists:
#4) Add values of 'l1' and 'l2' nodes. along with 'carry'

#5) Computer the new 'carry': It is eaither 0 or 1

#6) Append the result to the 'curent' node

#7) Move '11', '12', and 'current' pointer forward

#Handle the Carry
#8) After the main loop, if there is a remaining 'carry' add a node with
#the value

#Return Result
#9) The result is in the 'next' node after the dummy head as the dummy head was just a placeholder

#Complexity Analysis
#
from tkinter.tix import ListNoteBook
from pyparsing import List, Optional, ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNoteBook]:
        #Set up the starting point (Dummy Head)
        #'dummyHead' is a placeholder node that helps
        #to easily return the head of the new linked
        #list we add the numbers
        
        #'current' - is a pointer that will track the
        #end of the new linked list as we add digits
        #to it
        dummyHead = ListNode(0)
        current = dummyHead
        
        #Initialization of the Carry
        #'carry' is a variable that will hold any over-
        #flow when two digits add up to 10 or more
        carry = 0
        
        #Looping through both linked lists
        #The loop will continue as long as there are more
        #nodes to process in either 'l1' or 'l2' or there
        #is a 'carry' from the last operation 
        while l1 != None or l2 != None or carry != 0:
            #Adding digits and carry
            #l1Val and l2Val get the current node values of
            #'l1' and 'l2' - If the node is 'None' > This 
            #means we have reached the end of the list > it
            #takes the value '0'
            
            #'columnSum' is the sum of 'l1Val', 'l2Val', and
            #any 'carry' from the previous operations 
            #'carry' > is updated for the next iteration - If
            #'columnSum' is 10 or greater - 'carry' will be 1
            #OTHERWISE it will be '0'
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            
            #Creating a New Node for the Sum
            #A new node is created with the digit value 'columnSum % 10'
            #which is the remainder when 'columnSum' is divided by '10'
            #This is effectively the 'ones' digit of the sum - The new node
            #is added to the end of the current result list '(current.next)'
            #and then current is updated to this new node
            newNode = ListNode(columnSum % 10)
            current.next = newNode
            current = newNode
            
            #Moving to the Next Digits
            #The pointers 'l1' and 'l2' are moved to the next node in their 
            #respective lists if there is a next node - otherwise that are 
            #set to none
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            #Returning the Result
            #After looping ends: all digits in the list have been processed
            #the method returns the next node after 'dummyHead' - which is the 
            #actual start of the new linked list
            return dummyHead.next
        
        
        '''How to Understand This as a Beginner'''
'''Think of l1 and l2 as two stacks of plates with numbers on them. You are stacking a new pile of plates (dummyHead) by taking the top plate from each pile (l1 and l2), adding the numbers, and possibly carrying a 1 if your hands are full. If you run out of plates in one pile, you just add from the remaining pile with any carry you have.

The dummyHead is like a placeholder on the table so you always remember where to start stacking the new pile from. After you're done, you show the pile starting from the first real plate, which is the next one after the placeholder.

As a beginner, you should remember that this approach is mimicking the addition you do with pen and paper, going digit by digit and carrying over when needed, but using nodes in a linked list instead of written numbers.'''