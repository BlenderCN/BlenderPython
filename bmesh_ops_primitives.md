### bmesh.ops  primitives
____

- bmesh.ops.create_grid  
- bmesh.ops.create_uvsphere  
- bmesh.ops.create_icosphere  
- bmesh.ops.create_monkey  
- bmesh.ops.create_cone  
- bmesh.ops.create_circle  
- bmesh.ops.create_cube  

Currently bpy docs lists the above primitives, but search the docs with `bmesh.ops.create` for the full list of primitives and their parameter lists.

To create a uv sphere with `bmesh.ops`:

```python
import bpy
import bmesh

def create_uv_sphere(name, u=5, v=4, d=1):
    # bmesh.ops.create_uvsphere also accepts a matrix keyword argument, 
    # which i've dropped from the example.
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=u, v_segments=v, diameter=d)
    
    # create new empty mesh and fill with uvsphere
    mesh = bpy.data.meshes.new(name + "_mesh")
    bm.to_mesh(mesh)
    bm.free()
    
    # create object and link to scene
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.objects.link(obj)
    return obj

create_uv_sphere('my_uvsphere', u=5, v=4, d=1)
    
```

During your experimentation you might encounter errors when you pick and mix which arguments to use. 
If you get `SyntaxError: non-keyword arg after keyword arg` it's [explained here in the python docs](https://docs.python.org/3.4/tutorial/controlflow.html#keyword-arguments). Reading that will increase your Python-fu! 
