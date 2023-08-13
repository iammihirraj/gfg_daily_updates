#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		xor_result=0
		for num in nums:
		    xor_result ^=num
		    
	    rightmost_set_bit = 1
	    while(xor_result & rightmost_set_bit) == 0:
	        rightmost_set_bit <<= 1
	    
	    unique_num1, unique_num2 = 0,0
	    for num in nums:
	        if (num & rightmost_set_bit) == 0:
	            unique_num1 ^= num
	            
            else:
                unique_num2 ^= num
                
        return[min(unique_num1, unique_num2), max(unique_num1, unique_num2)]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends