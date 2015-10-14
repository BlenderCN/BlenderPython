# Mesh

There are two ways to create `Mesh` data.  

- One relies on first defining all vertices / edges / faces in lists and then sending them to a function called `.from_pydata()`.
- The other grows the mesh in place by adding _vertex coordinates_ and _edge / face indices_ sequentially.

Both methods have strengths and weaknesses, picking which to use depends largely on what you're doing. 
- Are you create a mesh from scratch?
- Are you updating and existing mesh (possibly with new additional geometry)
- Are you purely updating vertex locations of an existing mesh.
- ..etc,..

## from_pydata

### snippet 1 (creating: Verts and Edges)
______

Date: October 2015

This method expects the `Mesh` object to be empty (more about that below). 

```python
# be in object mode with nothing selected.

import bpy

# create 4 verts, string them together to make 4 edges.
coord1 = (-1.0, 1.0, 0.0)
coord2 = (-1.0, -1.0, 0.0)
coord3 = (1.0, -1.0, 0.0)
coord4 = (1.0, 1.0, 0.0)

Verts = [coord1, coord2, coord3, coord4]
Edges = [[0,1],[1,2],[2,3],[3,0]]

mesh = bpy.data.meshes.new("Base_Data")
mesh.from_pydata(Verts, Edges, [])
mesh.update()

obj = bpy.data.objects.new("Base_Object", mesh)

scene = bpy.context.scene
scene.objects.link(obj)
obj.select = True
```

This snippet   
- adds a new empty mesh called 'Base_Data' to the `bpy.data` collection.
- pushes `Verts, Edges, and an empty list` onto the new empty Mesh
    - The empty list `[]` is because `from_pydata` expects 3 arguments, none are optional
    - You can choose to pass just _verts_, or just _verts + edges_ or just _verts + faces_ like:  

        ```python
        mesh.from_pydata(Verts, [], [])
        mesh.from_pydata(Verts, Edges, [])
        mesh.from_pydata(Verts, [], Faces)
        ```
    
    - In the event you want to add _some faces_ and _some edges_ you can of course do
          `mesh.from_pydata(Verts, Edges, Faces)`

### snippet 2 (creating: Verts and Quad Faces)
______

Date: October 2015

This method expects the `Mesh` object to be empty (more about that below). 
```python
import bpy

verts = [
    (1.0, 1.0, -1.0),
    (1.0, -1.0, -1.0),
    (-1.0, -1.0, -1.0),
    (-1.0, 1.0, -1.0),
    (1.0, 1.0, 1.0),
    (1.0, -1.0, 1.0),
    (-1.0, -1.0, 1.0),
    (-1.0, 1.0, 1.0)
]

faces = [
    (0, 1, 2, 3),
    (4, 7, 6, 5),
    (0, 4, 5, 1),
    (1, 5, 6, 2),
    (2, 6, 7, 3),
    (4, 0, 3, 7)
]

mesh = bpy.data.meshes.new("cube_mesh_data")
mesh.from_pydata(verts, [], faces)
mesh.update()

cube_object = bpy.data.objects.new("Cube_Object", mesh)

scene = bpy.context.scene  
scene.objects.link(cube_object)  
cube_object.select = True  
```        

This should make sense, and the way to make Triangles is to simply pass in sub-lists that index 3 vertices instead of 4. 

> You are permitted to mix Triangles and Quads in the Faces list.


## sequentially adding vertices/edges/faces
______



## Not an empty Mesh?

You will need to get rid of all geometry in the Mesh before you can use `.from_pydata` on it. This is one way to do it without using `bpy.ops`. Effectively using `Bmesh` to overwrite the `Mesh` data.

```python
import bpy
import bmesh

p = bpy.data.objects['Obj2']

def clear_mesh(mesh):
    bm = bmesh.new()
    bm.to_mesh(mesh)
    bm.free()

clear_mesh(p.data)
p.data.update()
```
