#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int data;
    struct node* left;
    struct node* right;
} node;

node* root;

node* newNode(int number) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = number;
    temp->left = temp->right = NULL;
}

node* createNode(node* root, int number) {
    if(root==NULL) {
        root = newNode(number);
        return root;
    }
    else if(number > root->data) {
        root->right = createNode(root->right, number);
    }
    else {
        root->left = createNode(root->left, number);
    }
}

void getNode(int number) {
    root = createNode(root, number);
}

int height(node* root) {
    int left, right;
    if(root==NULL) {
        return -1;
    }
    else {
        left = height(root->left);
        right = height(root->right);

        if(left>right) 
            return left+1;
        else
            return right+1;
    }
}

void printCurrentLevel(node* temp, int level) {
    if(temp==NULL) 
        return;

    else if(level == 0) {
        printf(" %d ", temp->data);
    }
    else if(level>0){
        printCurrentLevel(temp->left, level-1);
        printCurrentLevel(temp->right, level-1);
    }
}

void PrintLevelOrder(node* temp) {
    int h = height(temp);
    printf("Tree is: \n");
    for(int i=0;i<h;i++)
        printCurrentLevel(temp, i);

}

int main() {
    root = NULL;
    getNode(40);
    getNode(30);
    getNode(20);
    getNode(10);
    getNode(25);
    getNode(35);
    getNode(50);
    getNode(60);
    getNode(70);
    getNode(45);
    getNode(65);
    
    printf("Height: %d\n", height(root));
    PrintLevelOrder(root);
    return 0;
}