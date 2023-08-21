#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        ma = 0
        total = 0
        for i in range(n):
            a = 0
            b = 0
            for j in range(n):
                a += matrix[i][j]
                b += matrix[j][i]
            ma = max(ma,a,b)
            total += a
        ma = ma*n
        return ma-total

#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends