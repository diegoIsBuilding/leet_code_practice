#Concept
#When you  add numbers starting from the least significant digit (the right most digit)
#you sometimes get a sum that is 10 or greater, requiring you to carry the "excess" to 
#the next significant digit - In a linked list representing a number in reverse order
#this is like adding the values of corresponding nodes, keeping track of the carry and
#moving on to the next nodes

from tkinter.tix import ListNoteBook
from pyparsing import List, Optional, ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNoteBook]:
        