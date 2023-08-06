//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
class Solution{
public:
    long long int countStrings(string s){
        int res=1;
        int n=s.length();
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
            if(s[i]!=s[j]){
                res++;
                }
            }
        }
        return res;
    }
};

//{ Driver Code Starts.

int main(){
    int T;
    cin >> T;
    while(T--){
        string s; 
        cin >> s; 
        Solution obj;
        long long int ans = obj.countStrings(s);
        cout << ans << "\n";
    }
}

// } Driver Code Ends