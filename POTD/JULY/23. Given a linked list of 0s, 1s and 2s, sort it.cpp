//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;
/* Link list Node */
struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

struct Node *start = NULL;


// } Driver Code Ends
/*
 
  Node is defined as
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
    //Function to sort a linked list of 0s, 1s and 2s.
    Node* segregate(Node *head) {
        
        // Add code here
        if(!head || !head->next)
        return head;
        
        Node* zero_head = new Node(0);
        Node* one_head = new Node(0);
        Node* two_head = new Node(0);
        
        Node* zero_tail = zero_head;
        Node* one_tail = one_head;
        Node* two_tail = two_head;
        
        Node* current = head;
        
        while(current){
            if(current->data == 0){
                zero_tail->next = current;
                zero_tail = zero_tail->next;
            } else if(current->data ==1){
                one_tail->next = current;
                one_tail = one_tail->next;
            } else {
                two_tail->next = current;
                two_tail = two_tail->next;
            }
            
            current = current->next;
        }
        
        zero_tail->next = NULL;
        one_tail->next = NULL;
        two_tail->next = NULL;
        
        //linking them together
        if(one_head->next){
            zero_tail->next = one_head-> next;
            if(two_head->next){
                one_tail->next = two_head-> next;
            }
        } else {
            zero_tail->next = two_head->next;
        }
        
        Node* result_head = zero_head->next;
        delete zero_head;
        delete one_head;
        delete two_head;
        
        return result_head;
    }
};



//{ Driver Code Starts.

// Function to sort a linked list of 0s, 1s and 2s
void printList(struct Node *Node) {
    while (Node != NULL) {
        printf("%d ", Node->data);
        Node = Node->next;
    }
    printf("\n");
}

/* Drier program to test above function*/
void insert(int n1) {
    int n, value, i;
    // scanf("%d",&n);
    n = n1;
    struct Node *temp;
    for (i = 0; i < n; i++) {
        scanf("%d", &value);

        if (i == 0) {
            start = new Node(value);
            temp = start;
            continue;
        } else {
            temp->next = new Node(value);
            temp = temp->next;
            temp->next = NULL;
        }
    }
}

int main() {

    int n;

    int t;
    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);

        insert(n);
        Solution ob;
        struct Node *newHead = ob.segregate(start);
        printList(newHead);
    }

    return 0;
}
// } Driver Code Ends