class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.key, end=" ")
    inorder(temp.right)


def insert(temp, key):
    if not temp:
        root = Node(key)
        return
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(21)
    root.left.left = Node(12)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(8)

    print("Tree: ")
    inorder(root)

    key = 13
    insert(root, key)

    print("\nTree: ")
    inorder(root)
