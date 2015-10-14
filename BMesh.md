
Blender comes with a great set of templates for BMesh, I won't reproduce them here.  

  - _TextEditor -> Templates -> Python -> BMesh Simple_   
  - _TextEditor -> Templates -> Python -> BMesh Simple EditMode_  

### Snippet 1 (simple sequential geometry additions)

If the Object is in Object mode.
```python
import bpy
import bmesh

# Get the active mesh
mesh = bpy.data.objects['object_name'].data
bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(mesh)   # fill it in from a Mesh

# some aliases
verts = bm.verts
faces = bm.faces
edges = bm.edges

# a Triangle
v1 = verts.new((2.0, 2.0, 2.0))
v2 = verts.new((-2.0, 2.0, 2.0))
v3 = verts.new((-2.0, -2.0, 2.0))
bm.faces.new((v1, v2, v3))

# a Quad
v1 = verts.new((3.0, 2.0, -3.0))
v2 = verts.new((-3.0, 2.0, -3.0))
v3 = verts.new((-3.0, -2.0, -3.0))
v4 = verts.new((3.0, -2.0, -3.0))
bm.faces.new((v1, v2, v3, v4))

# an Edge
v1 = verts.new((0.0, 1.0, 1.0))
v2 = verts.new((0.0, 0.0, 1.0))
bm.edges.new((v1, v2))

bm.to_mesh(mesh)
bm.free()
mesh.update()
```