This is a crash course in the Python subset. If you already master these you should not waste time reading this, unless you want to check for typos or factual inaccuracies. 

| basic 1 | basic 2 | intermediate |
|---------|---------|--------------|
| [print](GeneralPythonSnippets#print) | [string manipulation](GeneralPythonSnippets#string-manipulation) | [decorators](GeneralPythonSnippets#decorators) |
| [integer](GeneralPythonSnippets#integer) | [for loop](GeneralPythonSnippets#for-loop) |  |
| [float](GeneralPythonSnippets#float) | [list comprehensions](GeneralPythonSnippets#list-comprehensions) |  |
| [string](GeneralPythonSnippets#string) | [while loop](GeneralPythonSnippets#while-loop) |  |
| [tuple](GeneralPythonSnippets#tuple) | [flow control](GeneralPythonSnippets#flow-control) |  |
| [list](GeneralPythonSnippets#list) | [try except](GeneralPythonSnippets#try-except) |  |
| [dictionary](GeneralPythonSnippets#dictionary) | [functions](GeneralPythonSnippets#functions) |  |
| [boolean](GeneralPythonSnippets#boolean) | [import libraries](GeneralPythonSnippets#import-libraries) |  |
| [if statements](GeneralPythonSnippets#if-statements) | [classes](GeneralPythonSnippets#classes) |  |
| [standard library](GeneralPythonSnippets#standard-library) |  |  |

### How to run this code  

(elaborate) : Open Blender, and get a Python console view open. You'll notice `>>>` , this is a prompt waiting for you to type stuff. What we'll be doing below is type stuff after the prompt, then hit Enter to run it.


###print

While you learn Python `print()` is your friend. It will try to display whatever is between the parenthesis `( )`.

```python
>>> print("Hello apprentice")
... Hello apprentice
```

I'll return to `print()` frequently on this page to show how to display information that you will find helpful while coding.

###integer

Whole numbers, positive or negative. You'll see plenty of these as you progress.
```python
# let's make a variable called hal
>>> hal = 3000
>>> print(hal * 3)
... 9000
```
###float

Numbers like these `100.0`, `0.0000003` and `34.4`. etc. You will often see unusual floats like `0.00200023423` when you expect to see just `0.002`, this is normal and will be explained later.  
You might also see scientific notation for small numbers namely `2e-7` which is equivalent to `0.0000002`.

A lot more can be said about _floats_ but it rarely makes sense to talk about them in isolation. You'll see more references to floats further down.

###string

The words you read right now are strings. In Python we express strings by wrapping them in single qoutes, double qoutes or tripple qoutes.
```python
>>> my_first_string = "I am a HAL 9000 computer"
>>> my_second_string = 'I am a HAL 9000 computer'
>>> my_third_string = """I am a HAL 9000 computer"""
```
You can add strings together, we call it 'concatenation':
```python
# notice the spaces at the end of string, why is that?
>>> var1 = "I am a "  
>>> var2 = "HAL "
>>> var3 = "9000 computer"
>>> print(var1 + var2 + var3)
... I am a HAL 9000 computer
```

to convert a non string to a string is done explicitly using `str()`:
```python
>>> some_number = 9000
>>> "Hal " + str(some_number) 
... "Hal 9000"`
```

Further _string manipulation_ is discussed at a later stage. Strings are used a lot in Python, but in Blender they're commonly used to name objects, data, or set the properties of data.

###tuple

This is a data type which is used to collect data. You'll see a tuple defined in various ways.

```python
>>> some_number = 20
>>> tuple_one = ('some_string', some_number, 0.3444)
... ('some_string', 20, 0.3444)
```
but it's OK to drop the surrounding parenthesis, the comma separator is most important
```python
>>> tuple_two = 'some_string', some_number, 0.3444
>>> tuple_two
... ('some_string', 20, 0.3444)
```
you'll also see it written this way, but it is not common.
```python
>>> tuple_three = tuple(['some_string', some_number, 0.3444])
```
A tuple is _immutable_. This means you can not change any of the members of the tuple, once it's created it is unchangeable - also if the tuple was made with variables. If you change a variable, the tuple's content is not updated.. see what happens when we update var2 to hold a new string `SAL `.

```python
>>> var1 = "I am a "
>>> var2 = "HAL "
>>> var3 = "9000 computer"
>>> tuple_four = var1, var2, var3
>>> tuple_four
... ('I am a ', 'HAL ', '9000 computer')
>>> var2 = 'SAL '
>>> var4
('I am a ', 'HAL ', '9000 computer')    
```
To change a tuple you must assign a new tuple by overwriting the tuple stored in `var4`.
```python
>>> var4 = (var1, var2, var3)
>>> var4
('I am a ', 'SAL ', '9000 computer')
```