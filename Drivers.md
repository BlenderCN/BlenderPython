I don't know a whole lot about these, and [the docs](https://www.blender.org/manual/animation/basics/drivers.html#driver-namespace) seem to do a good job of covering most things.

Find neat tricks in _TextEditor -> Templates -> Python -> Driver Functions_  
  
### Driver from Python file

This is the long way, the scenic route. Using a python expression from a file. Sometimes you'll have expressions that are a bit more complicated than what you can fit onto 1 line comfortably.

- Rightclick the property in question, choose Add Single Driver
- Open the Graph Editor, and switch to Drivers view
- select the driven property, and toggle the rightside panel
- Make a script in the Text Editor with content similar to this.

```python
import math
import bpy

def driver_func(current_frame):
    frames = 120   # <-- period.
    theta = math.pi * 2 / frames
    final = math.sin(current_frame % frames * theta)
    return final

# add function to driver_namespace
bpy.app.driver_namespace['driver_func'] = driver_func

```
If your driver has a python error, you can correct it and run the code again to overwrite 
the namespace key 'driver_func`. You can name this function whatever you wish, and can have as many of them as you need in the .blend.

![theimage](https://cloud.githubusercontent.com/assets/619340/10715506/092e8798-7b19-11e5-9570-421515d8849f.png)

### example 2 

This might be obvious, but let's be explicit about the possibilities. We can use Empties as dummy objects, and give them custom properties, and assign a Driver to the custom property. Drivers can execute pretty much anything, that means also updating multiple other objects.

![img this](https://cloud.githubusercontent.com/assets/619340/10812732/8a912810-7e19-11e5-866c-545b2975189a.png)

The following code randomizes the location of an object named 'Text' between frame 30 and 60. The return value of the _driver function_ is never used, it's the function body we care about.

```python
import math
import bpy
import random

def driver_func2(current_frame):
    
    obj = bpy.data.objects.get('Text')
    if not obj:
        return 0.0

    rnd = random.random
    if 30 < current_frame < 60:
        obj.location = rnd(), rnd(), rnd()
    else:
        if obj.location.length > 0.0001:
            obj.location = 0, 0, 0

    return 0.0

# add function to driver_namespace
bpy.app.driver_namespace['driver_func2'] = driver_func2
```