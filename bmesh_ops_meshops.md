`bmesh.ops` brings a lot of convenience and power to the scripter. All `bmesh.ops` can found in the current API  docs: [blender.org/api/blender_python_api_current/search.html?q=bmesh.ops](http://www.blender.org/api/blender_python_api_current/search.html?q=bmesh.ops)
  
bmesh.ops [docs have a few good examples](http://www.blender.org/api/blender_python_api_current/bmesh.ops.html?highlight=bmesh.ops#module-bmesh.ops) which are recommended reading. Additionally _TextEditor > Templates > Python_ has two _Bmesh Simple_ templates that show how to get the bmesh representation of an Object's mesh (both in edit mode and object mode). 

### Example 1 Recal Normals  

If you need to see them in context think about the following case. You have a bmesh generated procedurally and can't guarantee the direction of the faces (they might be pointing outwards or inwards depending on the order in which you specify the vertex indices for each face).
  
This shows how to:
  
1. Mesh to bmesh (bm) 
2. using bmesh.ops on the bm, 
3. pushing the bm back to the Mesh.


```python
import bpy
import bmesh

verts = [
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0)]

faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),  # reversed
    (0, 4, 5, 1),
    (1, 5, 6, 2),
    (2, 6, 7, 3),
    (4, 0, 3, 7)]

def make_object(name, verts, faces, normal_recalc=True):

    scn = bpy.context.scene

    mesh = bpy.data.meshes.new(name + "_Mesh")
    mesh.from_pydata(verts, [], faces) 
    mesh.update()

    if normal_recalc:
        bm = bmesh.new()
        bm.from_mesh(mesh)
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.to_mesh(mesh)
        bm.free()

    ob = bpy.data.objects.new(name, mesh)
    scn.objects.link(ob)

make_object('my_cube', verts, faces)
# make_object(name, verts, faces, normal_recalc=False)
```

The extra bmesh operation is what recalculates the face normals. This does a good job of making the face directions consistent with surrounding faces. 

### Example 2 Doubles and Normals (chained bmesh.ops)

```python
import bpy
import bmesh

for obj in bpy.context.selected_objects:

    bm = bmesh.new()   # create an empty BMesh
    bm.from_mesh(obj.data)   # fill it in from a Mesh

    d = 0.0001
    bm_verts = bm.verts[:]
    bmesh.ops.remove_doubles(bm, verts=bm_verts, dist=d)

    bm_faces = bm.faces[:]
    bmesh.ops.recalc_face_normals(bm, faces=bm_faces)

    bm.to_mesh(obj.data)
    bm.free()
```

### Example 3 equivalent of screw modifier using bmesh.ops

```python
import bpy
import bmesh
from bmesh.ops import spin
import math


def lathe_geometry(bm, cent, axis, dvec, angle, steps, remove_doubles=True, dist=0.0001):
    geom = bm.verts[:] + bm.edges[:]

    # super verbose explanation.
    spin(
        bm, 
        geom=geom,         # geometry to use for the spin
        cent=cent,         # center point of the spin world
        axis=axis,         # axis, a (x, y, z) spin axis
        dvec=dvec,         # offset for the center point
        angle=angle,       # how much of the unit circle to rotate around
        steps=steps,       # spin subdivision level 
        use_duplicate=0)   # include existing geometry in returned content

    if remove_doubles:
        bmesh.ops.remove_doubles(bm, verts=bm.verts[:], dist=dist)

obj = bpy.data.objects['Graph']
bm = bmesh.new()
bm.from_mesh(obj.data)

axis = (1,0,0)
dvec = (0,0,0)
angle = 2*math.pi
steps = 20
cent = obj.location

lathe_geometry(bm, cent, axis, dvec, angle, steps, remove_doubles=True, dist=0.0001)

bm.to_mesh(obj.data)
bm.free()
```