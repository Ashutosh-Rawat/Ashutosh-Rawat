#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node* left;
    struct node* right;
} node;

node* root;

node* getNode(int data) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = data;
    temp->left = temp->right = NULL;
    return temp;
}

node* InsertNode(node* root, int number) {
    if(root == NULL) {
        root = getNode(number);
        return root;
    }
    else if(number>root->data) {
        root->right = InsertNode(root->right, number);
    }
    else {
        root->left = InsertNode(root->left, number);
    }
}

void createNode(node** rootpoint, int number) {
    root = InsertNode(*rootpoint, number);
}

void FindMaxMin(node* pointer) {
    node* pointer2 = pointer;
    while(pointer->right!=NULL) {
        pointer = pointer->right;
    }
    printf("Max number: %d\n", pointer->data);

    while(pointer2->left!=NULL) {
        pointer2 = pointer2->left;
    }
    printf("Min number: %d\n", pointer2->data);
}

int main() {
    root = NULL;
    createNode(&root, 40);
    printf("%d\n", root->data);
    createNode(&root, 30);
    printf("%d\n", root->left->data);
    createNode(&root, 50);
    printf("%d\n", root->right->data);
    createNode(&root, 80);
    printf("%d\n", root->right->right->data);
    FindMaxMin(root);    
    return 0;
}