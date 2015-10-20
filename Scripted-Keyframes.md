### Snippet 1 (scripted turntable

Parent camera to an empty, keyframe the rotation of the empty.

```python
import math
import bpy

def add_cam(location, rotation):
    bpy.ops.object.camera_add(location=location, rotation=rotation)
    return bpy.context.active_object

def add_empty(location):
    bpy.ops.object.empty_add(location=location)
    return bpy.context.active_object    

cam = add_cam(location=(0, -5, 0), rotation=(math.pi/2, 0, 0))
empty = add_empty(location=(0, 0, 0))
cam.parent = empty

num_frames = 90
gamma = math.pi * 2 / num_frames
for i in range(1, num_frames+1):
    empty.rotation_euler[2] = gamma * i
    empty.keyframe_insert(data_path='rotation_euler', frame=i, index=-1) 
```

>  See: [this page](https://github.com/zeffii/BlenderPythonRecipes/wiki/Empty-(null-object)) for more ways to create an Empty