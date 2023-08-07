#User function Template for python3

from typing import List
import sys

sys.setrecursionlimit(10**6)

class Solution:
    def reverse(self, St: List[int]):
        #code here
        #User function Template for python3
        def insert_at_bottom(stack, item):
            if not stack:
                stack.append(item)
            else:
                temp = stack.pop()
                insert_at_bottom(stack, item)
                stack.append(temp)

        if St:
            temp = St.pop()
            self.reverse(St)
            insert_at_bottom(St, temp)