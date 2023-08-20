#User function Template for python3
class Solution:


    def generateNextPalindrome(self,num, n ) :
        # code here
        flag = 0
        l = 0
        r = n - 1

        while l < r:
            if num[l] < num[r]:
                flag = -1
            elif num[l] > num[r]:
                flag = 1
            num[r] = num[l]
            l += 1
            r -= 1
        
        if flag == 0 or flag == -1:
            l = (n - 1) // 2
            while l >= 0:
                if num[l] < 9:
                    num[l] += 1
                    num[n - l - 1] = num[l]
                    return num
                else:
                    num[l] = 0
                    num[n - l - 1] = num[l]
                l -= 1
            return [1] + [0] * (n - 1) + [1]
        else:
            return num





#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends