I don't know a whole lot about these, and the docs seem to do a good job of covering most things.

### Driver from Python file

This is the long way, the scenic route. Using a python expression from a file.

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

# bpy.app.driver_namespace.clear()   <- don't! do this it will clear all convenience functions.
# better clear the namespace entry by name.
```
![theimage](https://cloud.githubusercontent.com/assets/619340/10715506/092e8798-7b19-11e5-9570-421515d8849f.png)