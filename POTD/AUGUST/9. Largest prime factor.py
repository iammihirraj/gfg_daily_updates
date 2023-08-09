#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        largest_factor = 1
        
        while N % 2 ==0:
            largest_factor = 2
            N //=2
            
        for i in range(3, int(N**0.5) + 1, 2):
            while N % i == 0:
                largest_factor = i
                N //=i
                
        if N > 2:
            largest_factor=N
            
        return largest_factor
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends