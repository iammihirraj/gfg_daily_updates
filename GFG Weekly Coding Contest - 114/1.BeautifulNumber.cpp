//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    bool beautifulNumber(int n) {
        // code here
        unordered_set<int>visited;
        while(n != 1){
            n = calculate_sum_of_squares(n);
            if(visited.find(n) != visited.end()){
                return false;
            }
            visited.insert(n);
        }
        return true;
    }
    int calculate_sum_of_squares(int num){
        int sum_of_squares=0;
        while(num>0){
            int digit = num % 10;
            sum_of_squares += digit * digit;
            num /= 10;
        }
        return sum_of_squares;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int n;
        scanf("%d",&n);
        
        Solution obj;
        bool res = obj.beautifulNumber(n);
        if(res) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
        
    }
}

// } Driver Code Ends