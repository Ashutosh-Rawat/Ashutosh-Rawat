#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node* left;
    struct node* right;
} node;

node* root;

node* newNode(int number) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = number;
    temp->left = NULL;
    temp->right = NULL;
}

int main() {
    root = NULL;
    root = newNode(50);
    root->left = newNode(40);
    root->left->left = newNode(30);
    root->left->left->left = newNode(20);
    root->left->left->left->left = newNode(10);
    
    root->right = newNode(60);
    root->right->right = newNode(70);
    root->right->right->right = newNode(80);

    root->right->left = newNode(55);
    root->right->left->right = newNode(56);
    root->left->right = newNode(45);
    root->left->right->left = newNode(42);

    printf("root: %d\n", root->data);

    printf("root->left: %d\n", root->left->data);
    printf("root->left->right: %d\n", root->left->right->data);
    printf("root->left->left: %d\n", root->left->left->data);

    printf("root->right: %d\n", root->right->data);
    printf("root->right->left: %d\n", root->right->left->data);
    printf("root->right->right: %d\n", root->right->right->data);
    return 0;
}