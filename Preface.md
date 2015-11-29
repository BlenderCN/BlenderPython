Welcome to this wiki/repository of Blender related python snippets. 

### First let's get the elephant out of the room

I might think of more things to say here at a later point but for now I want to stress that all this code is [licensed GPL3](). What does that mean? It means I would appreciate when you copy my code verbatim or (large sections) that you include the GPL3 license prominently in your add-on if you distribute it to others. I won't be bothered if you choose to ignore the licensing, but it's a politeness and people might call you out on it.

### OK. I get it, let's rock!

This wiki is intended to be only part of the learning process. If you already master Python I recommend going straight to [finding the docs](Preface#finding-docs) below. If that's not you and you don't know your way around Python's standard library then please do read on. 

I've included a section in the Introduction called [General Python Snippets](GeneralPythonSnippets), it covers the most important parts of Python that you need to be comfortable with before doing any Blender scripting. The rest of the _Blender Recipes_ on this wiki assume you know that subset of Python.

(insert section here)  
  
I can show you endless examples of how to do things, but eventually you need to 'close the book' and get acquainted with the process of finding documentation and experimenting with Python and Blender's API till you find a workflow that works for you.

### Finding docs

In 2015 we got version independent docs:

    http://www.blender.org/api/blender_python_api_current/ 
    http://www.blender.org/api/blender_python_api_current/search.html?q=bmesh 
    http://www.blender.org/api/blender_python_api_current/mathutils.geometry.html 

I found the process of finding docs was a little slow so I coded an addon that uses Blender's Python console to execute non-python commands (Ctrl+Enter vs Enter). 