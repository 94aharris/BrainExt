# Python Basics #

## Links ##

- [W3 Schools Python](https://www.w3schools.com/python/python_for_loops.asp)
- [Python Zero to Mastery](https://github.com/kamranahmedse/developer-roadmap)
- [HackerRank Python](https://www.hackerrank.com/domains/python)

## Learning Checklist ##

- [ ] Simple Logic, Function setup, Error Handling, Flow Control
- [ ] Objects and Polymorphism
- [ ] Network Interfaces
- [ ] All the methods of the 4 data types

## Python 'Gotchas' ##

- Indentation...
- remember the :
- Case Sensitive Methods and Functions

## Some Info ##

- All Built in Data Types
  - Text
    - str
  - Numeric
    - int, float, complex
  - Sequence
    - list, tuple, range
  - Mapping
    - dict
  - Set
    - set, frozenset
  - Boolian
    - bool
  - Binary
    - bytes, bytearray, memoryview

- 4 Colllection Types
  - Set
    - Store single multiple items in a single variable
    - unorderd, unindexed, do not allow duplicates (see unordered)
    - written with {} braces
  - List (array)
    - ordered, changeable, and allow duplicates
    - written with [] brackets
  - Dictionary (hashtable)
    - key value pairs
    - ordered, changeable, and does not allow duplicates
  - Tuple
    - ordered, unchangeable, and allow duplicates
    - written with () brackets

## Type-Specific Methods ##

- type specific method operations generally only work on that type (e.g. strings) and nothing else
- As a rule of thumb the toolset is layered: 
  - Generic operations that span multiple types are built-in functions (`len(strvar)` and `len(arrvar)`)
  - Type-specific operations are method calls (`srtvar.upper()`)
  
## Logic Parsing ##

```python
def isMyName(name):
    if (name.lower() == "Anthony") : return True
    else : return False
```

- if statements are evaluated left first then (if false) the right is evaluated. thats why something like the below will **not** work (you will get an exception)

```python
if not person or person.name == 'bob'
```

## Error Raising ##

```python
raise Exception('This is a Generic Exception Which is bad')
raise ValueError('This is a specific Exception which is better')
```

## Incrent Operators ##

- Python does not use ++ or --
- Use `var += 1` and `var -= 1` instead

## Comparison Operators ##

- Assignment `=`
- Equality `==`
- Less Than `<`
- Greater Than `>`
- And `and`
- or `or`

## Strings ##

- length
  - `len(stringvar)`
- lower / uppercase
  - `string.lower()` 
  - `string.upper()`
- Convert an integer to a string
  - use `str()`
  
```python
a = [1,2,3,4]
strvar = ""
for i in a
  strvar += str(a[i])
  strvar += " "
  i += 1
print(strvar)
```

- String interpolation with fstrings
  - `stringvar = f"My Name Is {namevar}"`
- String Trimming
  - remove leading and trailing whitespace 
    - `stringvar.strip()`
  - remove leading (left) whitespace
    - `stringvar.lstrip()`
  - remove trailing (right) whitespace
    - `stringvar.rstrip()`

## Math ##

- Basic Rounding
  - general rounding `Math.round(numvar)`
  - round down to whole `Math.floor(numvar)`
  - round up to whole `Math.ceil(numvar)`
- Sum of Array containing integers
  - `sum(arrvar)`
- Min/Max
  - Return the max or min of passed values (good for preventing array overrun)
  - `max(i-2,0)` - prevent an iterator from going below 0 on an array (out of bounds)
- Absolute Value
  - Return the absolute value (e.g. 1 = 1 ; -1 = 1) of a value
  - `abs(num)`

## Loops ##

  While

```python
while (i < len(arrvar)) :
  print(i)
```  

  For

```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

## List (Arrays) ##

- **Add to an array**
  - at end
    - `arrvar.append("value")`
  - at given index (i)
    - `arrvar.insert(i,"value")`
  - add list to list
    - `arrvar.extend([1,2,3])`

- **Array Splicing**
  
```python
a = [1,2,3,4,5] 
shift = 4
a[shift:]
>>[5]
a[:shift]
>>[1, 2, 3, 4]
a[shift:] + a[:shift]
>>[5, 1, 2, 3, 4]

+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

- **Compare Arrays for Intersections**
  - Convert to a 'Set' then compare

```python
arrvar1 = [1,2,3,4,5]
arrvar2 = [5,6,7,8,9]

set(arrvar1) & set(arrvar2)
>> {5}

s1 = "anthony"
s2 = "hello"
set(s1) & set(s2)
>> {'h','o'}
```

- **List Sorting**
  - `listvar.sort()`
    - This does not have to be assigned to anything, python lists are mutable
    - This works on a multi dimensional array as well (automatically sorts on first column)

    ```python
    >>> arr = [[1,0],[7,1],[5,1],[3,0]]
    >>> arr
    [[1, 0], [7, 1], [5, 1], [3, 0]]
    >>> arr.sort()
    >>> arr
    [[1, 0], [3, 0], [5, 1], [7, 1]]
    ```
  - `sorted()` function
    - Function which returns a new sorted list from items in an iterable
    - optional arguments
      - cmp - comparison function of two arguments to compare two iterable elements
      - key - specifies a function that is used to extract the comparison key (e.g. key=len)
      - reverse - boolian if set to true list elements sorted as if each comparison was reversed
    - **Hot Tip:** use key with a lambda function of lambda x: x[i] to sort a multidimensional list iterable by the ith element on the inner list
    
    ```python
    >>> arr = [['a',2],['b',0],['c',1]]
    >>> sorted_multi_list = sorted(multi_list, key=lambda x: x[1])
    >>> sortedList = sorted(arr, key=lambda x: x[1])
    >>> print(sortedList)
    [['b', 0], ['c', 1], ['a', 2]]
    ```

## Sets ##

- Used to store multiple items in single varible
- Unordered
- Unindexed
- Do NOT allow duplicates
- Unchangable
  - `thisset = {"apple","banana","cherry"}`
- Methods
  - add()
  - clear()
  - copy()
  - difference()
  - difference_update()
  - discard()
  - intersection()
  - intersection_update()
  - isdisjoint()
  - issubset()
  - issuperset()
  - pop()
  - remove()
  - symmetric_difference()
  - symmectric_difference_update()
  - union()
  - update()

## Tuple ##

## Dictionary (Hashtable) ##

*leet code tip* - Dictionaries are case sensitive, if a question mentions case sensitive lookups specifically, may be wanting a dictionary

- Key Value Pairs
  - `dict = {'key1': 'Valuex'}`

## Classes ##

**Note:** if you get "[takes 1 positional argument but 2 were given"](https://careerkarma.com/blog/python-takes-one-positional-argument-but-two-were-given/) often raised when you try to pass an argument through a method in a class without adding self as an argument

- Pros
  - Provide Inheritance
  - Provide Composition
  - Multiple instances
  - customization via inheritance
  - Operator overloading

- Methods
  - Made sure you have self as an input or you'll get an error
  
```python
class Dog:

    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
      self.name = name # new name for each dog
      self.tricks = [] # new empty listing for each dog

    def add_trick(self, trick):
      self.tricks.append(trick)
```

```python
>> d = Dog('Fido')
>> d.add_trick('roll over')
>> d.tricks
['roll over']
```

## Important Python Statements ##

- Assignment
  - `intvar = 1`
- Calls and expressions
  - `log.write("blah")`
- print calls
  - `print (f"hello {name}")`
- if/elif/else
- for/else
- while/else
- pass
- break
- continue
- def
- return
- yield
- global
- nonlocal
- import
- from
- class
- try/except/finally
- raise
- assert
- with/as
- del

## Null ##

- Python does not have `null` it uses `None`