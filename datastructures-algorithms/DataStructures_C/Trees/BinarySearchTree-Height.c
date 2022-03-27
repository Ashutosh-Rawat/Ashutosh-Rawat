#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node* left;
    struct node* right;
} node;

node* root;

node* getNode(int number) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = number;
    temp->left = temp->right = NULL;
    return temp;
}

node* addNode(node* root, int number) {
    if(root==NULL) {
        root = getNode(number);
        return root;
    }
    else if(root->data < number) {
        root->right = addNode(root->right, number);
    }
    else {
        root->left = addNode(root->left, number);
    }
}

void createNode(int number) {
    root = addNode(root, number);
}

int findHeight(node* root) {
    int leftHeight, rightHeight;
    if(root==NULL) {
        return -1;   // -1 for considering that leaf nodes have 0 height and null childs of leaf have height -1
    }
    else {
        leftHeight = findHeight(root->left);
        rightHeight = findHeight(root->right);
        return (__max(leftHeight,rightHeight)+1);
    }
}

int main() {
    root = NULL;
    createNode(40);
    createNode(30);
    createNode(20);
    createNode(50);
    createNode(32);
    createNode(34);
    createNode(36);
    createNode(37);
    printf("\nroot->left->right->right->right->right->data : %d\n", root->left->right->right->right->right->data);
    printf("Height : %d\n", findHeight(root));
    return 0;
}