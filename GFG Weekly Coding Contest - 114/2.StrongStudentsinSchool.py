#User function Template for python3

class Solution:
    def diffSum(self, n, m, arr): 
        # code here 
        arr.sort()
        max_difference = 0
        for i in range(m):
            max_difference += arr[n - i - 1] - arr[i]
        return max_difference


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == "__main__": 
	t = int(input())
	for _ in range(t):
		line = list(map(int, input().strip().split()))
		n = line[0]
		m = line[1]
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		print(ob.diffSum(n,m,arr))
# } Driver Code Ends