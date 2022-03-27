#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node *left, *right;
} node;

node* root;

node* newNode(int number) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = number;
    temp->right = temp->left = NULL;
    return temp;
}

node* InsertNode(node* root, int number) {
    if(root==NULL) {
        root = newNode(number);
        return root;
    }
    else if(root->data>=number) {
        root->left = InsertNode(root->left, number);
        return root;
    }
    else {
        root->right = InsertNode(root->right, number);
        return root;
    }
}

void getNode(int number) {
    root = InsertNode(root, number);
}

node* findMin(node* root) {
    if(root->left==NULL) 
        return root;
    
    else {
        findMin(root->left);
    }
}

node* DeleteNode(node* root, int number)
{
    if (root == NULL)
        return root;

    if (number<root->data)
        root->left = DeleteNode(root->left,number);

    else if (number>root->data)
        root->right = DeleteNode(root->right,number);
 
    // if number is same as root's data, then this is the node to be deleted

    else {
        // node with only one child or no child
        if (root->left == NULL) {
            node* temp = root->right;
            free(root);
            return temp;
        }
        else if (root->right == NULL) {
            node* temp = root->left;
            free(root);
            return temp;
        }
 
        // node with two children:
        // Get the inorder successor (smallest in the right subtree)
        node* temp = findMin(root->right);
 
        // Copy the inorder
        // successor's content to this node
        root->data = temp->data;
 
        // Delete the inorder successor
        root->right = DeleteNode(root->right,temp->data);
    }
    return root;
}

void PrintInorder(node* root) {
    if(root==NULL) return;
    else {
        if(root->left!=NULL) {
            PrintInorder(root->left);
        }
        printf("%d  ", root->data);
        if(root->right!=NULL) {
            PrintInorder(root->right);
        }
    }
}

int main() {
    getNode(40);
    getNode(30);
    getNode(20);
    getNode(10);
    getNode(25);
    getNode(35);
    getNode(15);
    getNode(50);
    getNode(60);
    getNode(70);
    getNode(45);
    getNode(55);
    getNode(65);
    PrintInorder(root);
    printf("\n");
    root = DeleteNode(root, 70);
    PrintInorder(root);
    printf("\n");
    root = DeleteNode(root,65);
    PrintInorder(root);
    printf("\n");
    root = DeleteNode(root, 30);
    PrintInorder(root);
    return 0;
}