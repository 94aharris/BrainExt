# Python Basics #

## Links ##

- [W3 Schools Python](https://www.w3schools.com/python/python_for_loops.asp)
- [Python Zero to Mastery](https://github.com/kamranahmedse/developer-roadmap)

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

- 4 DataTypes
  - Set 
  - List (array)
  - Dictionary (hashtable)
  - Tuple
  
## Logic Parsing ##

    def isMyName(name):
        if (name.lower() == "Anthony") : return True
        else : return False

- if statements are evaluated left first then (if false) the right is evaluated. thats why something like the below will **not** work (you will get an exception)

      if not person or person.name == 'bob'

## Error Raising ##

    raise Exception('This is a Generic Exception Which is bad')
    raise ValueError('This is a specific Exception which is better')

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
  

         a = [1,2,3,4]
         strvar = ""
         for i in a
            strvar += str(a[i])
            strvar += " "
            i += 1
        print(strvar)

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

## Loops ##

  While

    while (i < len(arrvar)) :
      print(i)
  
  For

    for x in range(6):
      print(x)
    else:
      print("Finally finished!")

## List (Arrays) ##

- Array Slicing
- Add to an array
  - at end
    - `arrvar.append("value")`
  - at given index (i)
    - `arrvar.insert(i,"value")`
  - add list to list
    - `arrvar.extend([1,2,3])`
- Array Splicing

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
- Compare Arrays for Intersections
  - Convert to a 'Set' then compare
      
      arrvar1 = [1,2,3,4,5]
      arrvar2 = [5,6,7,8,9]

      set(arrvar1) & set(arrvar2)
      >> {5}

      s1 = "anthony"
      s2 = "hello"
      set(s1) & set(s2)
      >> {'h','o'}

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

## If ##
