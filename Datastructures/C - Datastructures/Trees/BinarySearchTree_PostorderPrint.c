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
    temp->left = temp->right = NULL;
    return temp;
}

node* InsertNode(node* root, int number) {
    if(root==NULL) {
        root = newNode(number);
        return root;
    }
    else if(number>root->data) {
        root->right = InsertNode(root->right, number);
    }
    else {
        root->left = InsertNode(root->left, number);
    }
}

node* getNode(int number) {
    root = InsertNode(root, number);
}

void PrintPostorder(node* root) {
    if(root==NULL) return;
    else {
        if(root->left!=NULL) {
            PrintPostorder(root->left);
        }
        if(root->right!=NULL) {
            PrintPostorder(root->right);
        }
        printf("%d  ", root->data);
    }
}

int main() {
    root = NULL;
    getNode(40);
    getNode(30);
    getNode(20);
    getNode(35);
    getNode(10);
    getNode(25);
    getNode(50);
    getNode(60);
    getNode(55);
    getNode(50);
    getNode(45);
    getNode(75);

    PrintPostorder(root);
    return 0;
}
