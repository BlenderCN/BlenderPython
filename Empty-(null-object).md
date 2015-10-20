Empties are used for a lot of reasons:  

- as parents
- for Mirror Modifier, as _Mirror Object_
- for Array Modifier, as _Object Offset_
- for Screw Modifier, as _Axis Object_
- etc...

option 1:
```python
bpy.ops.object.add(type='EMPTY', location=world_coord, rotation=(0, 0, 0))
```
option 2 (useful if you want to avoid using bpy.ops):
```python
scene = bpy.context.scene
objects = bpy.data.objects
empty = objects.new("empty_name", None)
scene.objects.link(empty)
scene.update()
```
