# Python Basics #

## Links ##

- [W3 Schools Python](https://www.w3schools.com/python/python_for_loops.asp)
- [Python Zero to Mastery](https://github.com/kamranahmedse/developer-roadmap)

## Learning Checklist ##

- [ ] Simple Logic, Function setup, Error Handling, Flow Control
- [ ] Objects and Polymorphism
- [ ] Network Interfaces

## Logic Parsing ##

    def isMyName(name):
        if (name.lower() == "Anthony") : return True
        else : return False

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

## Math ##

- Basic Rounding
  - general rounding `Math.round(numvar)`
  - round down to whole `Math.floor(numvar)`
  - round up to whole `Math.ceil(numvar)`

## Loops ##

  While

    while (i < len(arrvar)) :
      print(i)
  
  For

    for x in range(6):
      print(x)
    else:
      print("Finally finished!")