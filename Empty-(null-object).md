Empties are used for a lot of reasons:  

- as parents
- for Mirror Modifier, as _Mirror Object_
- for Array Modifier, as _Object Offset_
- for Screw Modifier, as _Axis Object_
- etc...

option 1:
```python
bpy.ops.object.add(type='EMPTY', location=world_coord, rotation=(0, 0, 0))

# the drawback is that if you need to a reference to the object you have to 
# get it manually using active_object. 
# (useful for setting a name..or other properties)
mt = bpy.context.active_object
mt.name = 'empty_name'  
mt.location = vert_coordinate
mt.empty_draw_size = 2   
```
option 2 (useful if you want to avoid using bpy.ops):
```python
scene = bpy.context.scene
objects = bpy.data.objects
empty = objects.new("empty_name", None)
scene.objects.link(empty)
scene.update()
```
