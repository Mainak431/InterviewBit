/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int i;
int last;
void inorder(TreeNode* A, vector<int> &v) {
    if (A == NULL || i < 0) {
        return;
    }
    inorder(A->left, v);
    if (i != 0) {
        if (last > A->val) {
            v.push_back(A->val);
            v.push_back(last);
            
        }
    }
    i++;
    last = A->val;
    
    inorder(A->right, v);
}
vector<int> Solution::recoverTree(TreeNode* A) {
    vector<int> res;
    vector<int> v;
    i = 0;
    last = 0;
    inorder(A, v);
    sort(v.begin(), v.end());
    res.push_back(v[0]);
    res.push_back(v[v.size() - 1]);
    return res;
}
