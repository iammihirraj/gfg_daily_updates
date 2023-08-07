#User function Template for python3
class Solution:
    
    def SolveSudoku(self,grid):
        def isValid(num,grid,row,col):
            for i in range(9):
                if(grid[row][i]==num):
                    return False
            
            for i in range(9):
                if(grid[i][col]==num):
                    return False
            
            rr=row-row%3
            cc=col-col%3
            
            for i in range(3):
                for j in range(3):
                    if(grid[rr+i][cc+j]==num):
                        return False
            
            return True
            
            
        for i in range(9):
            for j in range(9):
                if(grid[i][j]==0):
                    for k in range(1,10):
                        if(isValid(k,grid,i,j)):
                            grid[i][j]=k
                            ans=self.SolveSudoku(grid)
                            if(ans): return True
                            else: grid[i][j]=0
    
                    return False         
        return True    
               
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=" ")

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends