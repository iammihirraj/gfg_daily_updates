//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};

void print(Node *root)
{
Node *temp = root;
while(temp!=NULL)
{
cout<<temp->data<<" ";
temp=temp->next;
}
}


// } Driver Code Ends
/*
The structure of linked list is the following

struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/
class Solution
{
    public:
    Node * removeDuplicates( Node *head) 
    {
      if(head==NULL)
        return NULL;
        
        Node* curr=head;
        unordered_map<int,int> mp;
        Node* anshead=NULL;
        Node* anscurr=NULL;
        while(curr!=NULL){
            mp[curr->data]++;
            if(mp[curr->data]<=1) {
                Node* newNode=new Node(curr->data);
                if(anshead==NULL){
                    anshead=newNode;
                    anscurr=newNode;
                }else{
                    anscurr->next=newNode;
                    anscurr=newNode;
                }
            }
            curr=curr->next;
    }
    return anshead;
    }
};


//{ Driver Code Starts.

int main() {
	// your code goes here
	int T;
	cin>>T;
	
	while(T--)
	{
		int K;
		cin>>K;
		struct Node *head = NULL;
        struct Node *temp = head;
 
		for(int i=0;i<K;i++){
		int data;
		cin>>data;
			if(head==NULL)
			head=temp=new Node(data);
			else
			{
				temp->next = new Node(data);
				temp=temp->next;
			}
		}
		
	    Solution ob;
		Node *result  = ob.removeDuplicates(head);
		print(result);
		cout<<endl;
		
	}
	return 0;
}
// } Driver Code Ends