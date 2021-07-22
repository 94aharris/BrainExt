# Algos and DataStructures #

## Resources ##

- [Big-O Simple Explanation](https://www.linkedin.com/pulse/big-o-notation-simple-explanation-examples-pamela-lovett/)

## General Algorithmic Concepts ##

## Big O ##

Space and time complexity of a solution as the input (n) gets larger. The 'Worse Case'

### Multi-Part Algorithms ###

- Multiply Big O when you do x for each y
  - Nested for loops
  - Double Loop with complexity of O(n) each is a total of O(n*n) = O(n^2)
- Add Big O when you do this then that
  - Do one thing after the other
  - Sort the array O(n log n) then traverse O(n) is O((n log n) + n) = O(n log n)

### O(1) - Constant Time ###

- constant time to run algorithm
- Math equations
- Print statements
- Hash access

### O(n) - Linear Time ###

- Time increases at same pace as input
- foreach, map, and reduce

### O(log n) - Logarithmic Time ###

- Running time in proportion to the Log of the input size
- run time barelly increases as you exponentially increase the input
- Binary Search

### O(n log n) - Asymptotic Time Complexity ###

- when you need to do work O(log n) for each item
- building perfectly balanced binary tree or traversing a binary tree
- Mergesort / quicksort

### O(n^2) - Quadratic Time ###

- Time is squared size of the output
- commonly double loop
- Bubble Sort

## Arrays and Strings ##

### Hash Tables ###

- Map key to value for efficient lookup
- Hashes the key into a code (int)
- Map the code (int) into an array index then use for lookup
- At each index is a linked list of values
- Assumed that lookup runtime is O(1) but high collision could theoretically be as high as O(n)

### Array List ###

- Resizable array
- Insertion is O(1) so inserting n items is O(n)

### Strings ###

- Immutable string copy can have bad performance
- Mutable strings or Stringbuilder is a better performance option

## Linked Lists ##

### Overview ###

- Sequence of nodes
- Singly Linked - each node points to the next
- Doubly Linked - each node points to the next and the previous
- You can add and remove items from the start and end of list in constant time

### Singly Linked List Example in Python ###

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self, data):
        end = Node(data)
        currentNode = self
        
        while (currentNode.next != None) :
            currentNode = currentNode.next
        
        currentNode.next = end
    
    def express(self):
        print(self.data)
```

### Runner Technique ###

- iterate through the linked list with two pointers simultaneously
- fast node and slow node

### Recursive Problem ###

- a number of linked list problems rely on recursion
- if you have problems solving a linked list problem, ctry exploring if a recursive approach will work
  
## Stacks and Queues ##

## Trees and Graphs ##

## Common Search Algorithms ##

## Recursion and Backtracking ##