#include<stdio.h>
#include<stdlib.h>

#define INVALID -255
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
    else if(root->data<number) {
        root->right = InsertNode(root->right,number);
        return root;
    }
    else {
        root->left = InsertNode(root->left,number);
        return root;
    }
}

void getNode(int number) {
    root = InsertNode(root,number);
}

void PrintInorder(node* root) {
    if(root==NULL) return;
    else {
        PrintInorder(root->left);
        printf("%d  ", root->data);
        PrintInorder(root->right);
    }
}

node* FindMin(node* root) {
    if(root->left==NULL) return root;
    else
        FindMin(root->left);
}

node* FindNode(node* root, int number) {
    if(root->data<number) 
        FindNode(root->right,number);
    else if(root->data>number) {
        FindNode(root->left,number);
    }
    else 
        return root;
}

int InorderSuccessor(node* root, int number) {
    node* current = FindNode(root, number);
    if(root==NULL) {
        return INVALID;
    }
    if(current->right!=NULL) {
        int min = FindMin(current->right)->data;
        return min;
    }
    else {
        node *successor=NULL;
        node *ancestor = root;
        while(current!=ancestor) {
            if(current->data<ancestor->data) {
                successor = ancestor;
                ancestor=ancestor->left;
            }
            else 
                ancestor = ancestor->right;
        }
        return successor->data;
    }
}

int main() {
    root = NULL;
    getNode(40);
    getNode(10);
    getNode(5);
    getNode(20);
    getNode(15);
    getNode(30);
    getNode(25);
    getNode(70);
    getNode(80);
    getNode(90);
    getNode(55);
    getNode(50);
    getNode(45);
    getNode(60);
    getNode(65);
    getNode(75);
    getNode(85);
    printf("\n");
    PrintInorder(root);
    printf("\n");
    printf("Inorder Sucessor of %d : %d\n", 10, InorderSuccessor(root, 10));
    printf("Inorder Sucessor of %d : %d\n", 25, InorderSuccessor(root, 25));
    printf("Inorder Sucessor of %d : %d\n", 20, InorderSuccessor(root, 20));
    printf("Inorder Sucessor of %d : %d\n", 15, InorderSuccessor(root, 15));
    printf("Inorder Sucessor of %d : %d\n", 30, InorderSuccessor(root, 30));
    printf("Inorder Sucessor of %d : %d\n", 65, InorderSuccessor(root, 65));
    printf("Inorder Sucessor of %d : %d\n", 70, InorderSuccessor(root, 70));

    return 0;
}

