## 1.Implement Binary tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

## 2.Find height of a given tree

class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
 
 
# function to calculate the height of a given binary tree
def height(root):
 
    if root is None:
        return 0
 
    return 1 + max(height(root.left), height(root.right))
 
if __name__ == '__main__':
 
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
 
    print('The height of the binary tree is', height(root))

 ## 3. Perform Pre-order, Post-order, In-order traversal

# Tree traversal in Python
class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)


def postorder(root):

    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def preorder(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

## 4.Function to print all the leaves in a given binary tree

class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# fun to creates and returns a new node
def newNode(data):
    temp = Node(data)
    return temp
 
# fun to print leaf nodes from left to right
def printleafNodes(root):
    if not root:
        return
    st = []
    st.append(root)
 
    while len(st) > 0:
        root = st.pop()
        if not root.left and not root.right:
            print(root.data, end=" ")
 
        if root.right:
            st.append(root.right)
        if root.left:
            st.append(root.left)
if __name__ == '__main__':
 
    # create a binary tree
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(5)
    root.right.right = newNode(8)
    root.right.left.left = newNode(6)
    root.right.left.right = newNode(7)
    root.right.right.left = newNode(9)
    root.right.right.right = newNode(10)
    printleafNodes(root)


 ## 5.   Implement BFS (Breath First Search) and DFS (Depth First Search)

 # BFS (Breath First Search) 

import collections
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)

 # DFS (Depth First Search)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')
