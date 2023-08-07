#User function Template for python3

class Solution:
    
    def swap(self, s, i, j):
        lst = list(s)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
    
    def generate_permutations(self, s, left, right, result):
        if left == right:
            result.append(s)
        else:
            for i in range(left, right + 1):
                s = self.swap(s, left, i)
                self.generate_permutations(s, left + 1, right, result)
                s = self.swap(s, left, i)
                
    def permutation(self,s):
        result = []
        n = len(s)
        self.generate_permutations(s, 0, n -1, result)
        return sorted(result)