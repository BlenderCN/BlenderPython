I don't know a whole lot about these, and [the docs](https://www.blender.org/manual/animation/basics/drivers.html#driver-namespace) seem to do a good job of covering most things.

Find neat tricks in _Templates -> Python -> Driver Functions_  
  
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