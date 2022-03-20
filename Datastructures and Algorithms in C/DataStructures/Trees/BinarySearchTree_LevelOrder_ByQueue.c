#include<stdio.h>
#include<stdlib.h>


/* Binary Search Tree starts from here */

typedef struct node {
    int data;
    struct node *left, *right;
} node;


/* code to create queue */

typedef struct queue {
    node* link;
    struct queue* next;
} queue;

queue *front, *rear;

void enque(node* newLink) {
    queue* temp = (queue*)malloc(sizeof(queue));
    temp->link = newLink;
    temp->next = NULL;

    if(front==NULL) {
        front = temp;
        rear = front;
        rear->next = NULL;
        return;
    }
    else {
        rear->next = temp;
        rear = rear->next;
    }
}
void deque() {
    if(front==rear) {
        front = front->next;
        rear = front;
        return;
    }
    front = front->next;
}


node* root;

node* newNode(int number) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = number;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

node* getNode(node* root, int number) {
    if(root==NULL) {
        root = newNode(number);
        return root;
    }
    else if(number>root->data) 
        root->right = getNode(root->right, number);
    else 
        root->left = getNode(root->left, number);
}

void createNode(int number) {
    root = getNode(root, number);
}

void PrintLevelOrder() {
    if(root==NULL) {
        return;
    }
    enque(root);
    while(front!=NULL) {
        node* current = front->link;
        printf("%d  ", current->data);
        if(current->left!=NULL)
            enque(current->left);
        if(current->right!=NULL)
            enque(current->right);
        deque(); 
    }
}

int main() {
    front = rear = NULL;
    root = NULL;

    createNode(40);
    createNode(30);
    createNode(20);
    createNode(10);
    createNode(25);
    createNode(35);
    createNode(50);
    createNode(45);
    createNode(60);
    createNode(55);
    createNode(70);

    PrintLevelOrder();
    return 0;
}
