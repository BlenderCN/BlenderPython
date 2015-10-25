Empties are used for a lot of reasons:  

- as parents
- for Mirror Modifier, as _Mirror Object_
- for Array Modifier, as _Object Offset_
- for Screw Modifier, as _Axis Object_
- etc...

option 1:
```python
bpy.ops.object.add(type='EMPTY', location=(0, 2, 1), rotation=(0, 0, 0))

# if you need a reference to the newly created Empty, then use the following.
# ( useful for setting a name..or other properties )
mt = bpy.context.active_object
mt.name = 'empty_name'  
mt.empty_draw_size = 2   
```
option 2 (useful if you want to avoid using bpy.ops):
```python
scene = bpy.context.scene
objects = bpy.data.objects
mt = objects.new("empty_name", None)
mt.location = (0, 2, 1)
mt.empty_draw_size = 2
scene.objects.link(mt)
scene.update()
```
option 2 may seem like more code, but you can set the name on the same line as the creation and you
get the reference at the same time.