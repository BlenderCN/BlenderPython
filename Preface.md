Welcome to this wiki/repository of Blender related python snippets. 

### First let's get the elephant out of the room

Are you free to use the code in this wiki for your own projects? Yes. My goal is to show working examples of the  current Blender Python API.

### OK. I get it, let's rock!

This wiki is intended to be only part of the learning process. If you already master Python I recommend going straight to [finding the docs](Preface#finding-docs) below. If that's not you and you don't know your way around Python's standard library then please do read on. 

I've included a section in the Introduction called [General Python Snippets](GeneralPythonSnippets), it covers the most important parts of Python that you need to be comfortable with before doing any Blender scripting. The rest of the _Blender Recipes_ on this wiki assume you know that subset of Python.

(insert section here)  
  
### Finding docs

I can show you endless examples of how to do things, but eventually you need to 'close the book' and get acquainted with the process of finding documentation and experimenting with Python and Blender's API till you find a workflow that works for you.

In 2015 we got version independent docs:

    http://www.blender.org/api/blender_python_api_current/ 
    http://www.blender.org/api/blender_python_api_current/search.html?q=bmesh 
    http://www.blender.org/api/blender_python_api_current/mathutils.geometry.html 

I found the process of finding docs was a little slow so I coded an addon that uses Blender's Python console to execute non-python commands (Ctrl+Enter vs Enter). 