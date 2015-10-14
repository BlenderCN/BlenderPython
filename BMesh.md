
Blender comes with a great set of templates for BMesh, I won't reproduce them here.  

  - _TextEditor -> Templates -> Python -> BMesh Simple_   
  - _TextEditor -> Templates -> Python -> BMesh Simple EditMode_  

### Snippet 1 (simple sequential geometry additions)

This example works if the Object is in _Object Mode_.

```python
import bpy
import bmesh

mesh = bpy.data.objects['object_name'].data
bm = bmesh.new()
bm.from_mesh(mesh)

# some aliases
verts = bm.verts
faces = bm.faces
edges = bm.edges

# a Triangle
v1 = verts.new((2.0, 2.0, 2.0))
v2 = verts.new((-2.0, 2.0, 2.0))
v3 = verts.new((-2.0, -2.0, 2.0))
faces.new((v1, v2, v3))

# a Quad
v1 = verts.new((3.0, 2.0, -3.0))
v2 = verts.new((-3.0, 2.0, -3.0))
v3 = verts.new((-3.0, -2.0, -3.0))
v4 = verts.new((3.0, -2.0, -3.0))
faces.new((v1, v2, v3, v4))

# an Edge
v1 = verts.new((0.0, 1.0, 1.0))
v2 = verts.new((0.0, 0.0, 1.0))
edges.new((v1, v2))

bm.to_mesh(mesh)
bm.free()
mesh.update()
```