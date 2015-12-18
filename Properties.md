Properties are what addons and operators use internally and on their UI. They are variables with potential side effects. An important feature of a property is they can call functions when their value is changed. To show what I mean let's take an abstract look.

```python
import bpy
from bpy.props import IntProperty
```
There are many more property types but the `IntProperty` is a convenient example. Take this hypothetical non-functioning piece of code

TODO

```python
import bpy
from bpy.props import IntProperty

def my_update(self, context):
   print(self)

bpy.types.Scene.some_int = IntProperty(min=0, max=4, name='some_int', update=my_update)

```
