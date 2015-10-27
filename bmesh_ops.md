Two main sections of bmesh.ops are _primitives_ and _mesh operations_.

### bmesh.ops  primitives
____

Search bpy docs for `bmesh.ops.create` for the full list primitives and their parameters lists.

To create a uv sphere without `bpy.ops`:
```python
import bpy
import bmesh

def create_uv_sphere(name, u=5, v=4, d=1):
    # bmesh.ops.create_uvsphere also accepts a matrix keyword argument, 
    # which i've dropped from the example.
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=u, v_segments=v, diameter=d)
    
    # create new empty mesh and fill with icosphere
    mesh = bpy.data.meshes.new(name + "_mesh")
    bm.to_mesh(mesh)
    bm.free()
    
    # create object and link to scene
    obj = bpy.data.objects.new("Base_Object", mesh)
    bpy.context.scene.objects.link(obj)

create_uv_sphere('my_uvsphere', u=5, v=4, d=1)
    
```
