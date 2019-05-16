#include <stack>
#include <stdio.h>
#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class BSTIterator {
private:
    std::stack<TreeNode*> TreeNodes;
    
public:
    BSTIterator(TreeNode* root) {
        while(root != NULL){
            this->TreeNodes.push(root);
            root = root->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        if(TreeNodes.empty()){
            return -1;
        }
        TreeNode* this_val = TreeNodes.top();
        TreeNodes.pop();
        if(this_val->right != NULL){
            TreeNode* tmp = this_val->right;
            while(tmp != NULL){
                this->TreeNodes.push(tmp);
                tmp = tmp->left;
            }
        }
        return this_val->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !TreeNodes.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

 int main(){
    TreeNode *TN3 = new TreeNode(3);
    TreeNode *TN7 = new TreeNode(7);
    TreeNode *TN9 = new TreeNode(9);
    TreeNode *TN15 = new TreeNode(15);
    TreeNode *TN20 = new TreeNode(20);
    TN7->left = TN3;
    TN7->right = TN15;
    TN15->left = TN9;
    TN15->right = TN20;
    BSTIterator* iterator = new BSTIterator(TN7);
    std::cout << iterator->next() << std::endl;    // return 3
    std::cout << iterator->next() << std::endl;    // return 7
    std::cout << iterator->hasNext() << std::endl; // return true
    std::cout << iterator->next() << std::endl;    // return 9
    std::cout << iterator->hasNext() << std::endl; // return true
    std::cout << iterator->next() << std::endl;    // return 15
    std::cout << iterator->hasNext() << std::endl; // return true
    std::cout << iterator->next() << std::endl;    // return 20
    std::cout << iterator->hasNext() << std::endl; // return false
    delete TN3;
    delete TN7;
    delete TN9;
    delete TN15;
    delete TN20;
}