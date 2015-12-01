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
...Hello apprentice
```

I'll return to `print()` frequently on this page to show how to display information that you will find helpful while coding.

###integer

Whole numbers, positive or negative. You'll see plenty of these as you progress.
```python
# let's make a variable called hal
>>> hal = 3000
>>> print(hal * 3)
...9000
```
###float

Numbers like these `100.0`, `0.0000003` and `34.4`. etc. You will often see unusual floats like '0.00200023423` when you expect to see just `0.002`, this is normal and will be explained later.  
You might also see scientific notation for small numbers namely `2e-7` which is equivalent to `0.0000002`