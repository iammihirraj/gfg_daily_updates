from collections import defaultdict

class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        hm = defaultdict(int)
        mod = pow(10, 9) + 7
        hm[0] = hm[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                hm[i] += hm[j] * hm[i - j - 1]
                hm[i] %= mod
        
        return hm[n]

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends