## 6. Find sum of all left leaves in a given Binary Tree

# A binary tree node
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def sumOfLeftLeaves(root):
    if(root is None):
        return
    stack = []  
    stack.append(root)
    sum = 0
    while len(stack) > 0:
        currentNode = stack.pop()
        if currentNode.left is not None:
            stack.append(currentNode.left)
            if currentNode.left.left is None and currentNode.left.right is None:
                sum = sum + currentNode.left.data
        if currentNode.right is not None:
            stack.append(currentNode.right)
    return sum
root = Node(20);
root.left= Node(9);
root.right   = Node(49);
root.right.left = Node(23);
root.right.right= Node(52);
root.right.right.left  = Node(50);
root.left.left  = Node(5);
root.left.right = Node(12);
root.left.right.right  = Node(12);
 
print('Sum of left leaves is {}'.format(sumOfLeftLeaves(root)))


## 7.Find sum of all nodes of the given perfect binary tree

import math
def sumNodes(l):
    leafNodeCount = math.pow(2, l - 1);
    sumLastLevel = 0;
    sumLastLevel = ((leafNodeCount *
        (leafNodeCount + 1)) / 2);
    sum = sumLastLevel * l;
    return int(sum);

# Driver Code
l = 3;
print (sumNodes(l));


## 8.Count subtress that sum up to a given value x in a binary tree

class Node:
 
    def __init__(self, data):
 
        self.data = data
        self.left = None
        self.right = None
 
def getNode(data):
    newNode = Node(data)
    return newNode
count = 0
ptr = None
def countSubtreesWithSumXUtil(root, x):
    global count, ptr
    l = 0
    r = 0
    if (root == None):
        return 0
    l += countSubtreesWithSumXUtil(root.left, x)
    r += countSubtreesWithSumXUtil(root.right, x)
    if (l + r + root.data == x):
        count += 1
    if (ptr != root):
        return l + root.data + r
    return count
# Driver code
if __name__ == '__main__':
 
    ''' binary tree creation
              5
            /  \
          -10   3
          / \  / \
          9 8 -4 7
    '''
 
    root = getNode(5)
    root.left = getNode(-10)
    root.right = getNode(3)
    root.left.left = getNode(9)
    root.left.right = getNode(8)
    root.right.left = getNode(-4)
    root.right.right = getNode(7)
 
    x = 7
    ptr = root
 
    print("Count = " + str(countSubtreesWithSumXUtil(
        root, x)))
    
## 9.Find maximum level sum in Binary Tree

# Create root of the tree:
root = None
globalMax = 2147483648

class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.val = v

def create_tree():
    global root
    root = Node(3)
    one = Node(2)
    two = Node(20)
    root.left = one
    root.right = two
    three = Node(7)
    four = Node(5)
    five = Node(-8)
    one.left = three
    two.left = four
    two.right = five

def find_max_sum(root):
    if root is None:
        return 0
    left = find_max_sum(root.left)
    right = find_max_sum(root.right)
    return_max = max(max(left, right) + root.val, root.val)
    maximum = max(return_max, left + right + root.val)
    global globalMax
    if maximum > globalMax:
        globalMax = maximum
    return return_max
create_tree()

find_max_sum(root)

print("Maximum possible value in a path: ", globalMax)

## 10.Print the nodes at odd levels of a tree

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    if (root == None):
        return
    if (isOdd):
        print(root.data, end = " ")
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
# Driver code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)
     

