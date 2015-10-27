
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

### Snippet 2 (pydata_from_bmesh)

This can be handy for debugging

```python
def pydata_from_bmesh(bm):
    v = [v.co[:] for v in bm.verts]
    e = [[i.index for i in e.verts] for e in bm.edges[:]]
    p = [[i.index for i in p.verts] for p in bm.faces[:]]
    return v, e, p
```

### Snippet 3 (bmesh_from_pydata):

if you've ever wondered what it might look like:
```python
import bmesh


def bmesh_from_pydata(verts=None, edges=None, faces=None):
    ''' verts is necessary, edges/faces are optional '''

    bm = bmesh.new()
    if not verts:
        return bm

    add_vert = bm.verts.new

    bm_verts = [add_vert(co) for co in verts]
    bm.verts.index_update()

    if faces:
        add_face = bm.faces.new
        for face in faces:
            add_face([bm_verts[i] for i in face])
        bm.faces.index_update()

    if edges:
        add_edge = bm.edges.new
        for edge in edges:
            edge_seq = bm_verts[edge[0]], bm_verts[edge[1]]
            try:
                add_edge(edge_seq)
            except ValueError:
                # edge exists!
                pass
        bm.edges.index_update()

    return bm

```

### Snippet 4 : Bmesh primitives

Bmesh has a number of primitive meshes just like `bpy.ops`, with the main difference being that you have to pass a receiver bmesh to fill with the geometry, and it doesn't create objects.


```python
import bmesh

def create_icospehere(subdiv, d):
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=subdiv, diameter=d)
    v, e, p = pydata_from_bmesh(bm)
    bm.free()
    return v, e, p
```