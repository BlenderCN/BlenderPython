# Mesh

There are two ways to create `Mesh` data.  

- One relies on first defining all vertices / edges / faces in lists and then sending them to a function called `.from_pydata()`.
- The other grows the mesh in place by adding _vertex coordinates_ and _edge / face indices_ sequentially.

Both methods have strengths and weaknesses, picking which to use depends largely on what you're doing.

### from_pydata
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

profile_mesh = bpy.data.meshes.new("Base_Profile_Data")
profile_mesh.from_pydata(Verts, Edges, [])
profile_mesh.update()

profile_object = bpy.data.objects.new("Base_Profile", profile_mesh)

scene = bpy.context.scene
scene.objects.link(profile_object)
profile_object.select = True
```



### sequentially adding vertices/edges/faces
______



### Not an empty Mesh?

There's no neat way to remove all vert/edges/faces data from an existing mesh without