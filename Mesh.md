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

mesh = bpy.data.meshes.new("Base_Data")
mesh.from_pydata(Verts, Edges, [])
mesh.update()

object = bpy.data.objects.new("Base_Object", mesh)

scene = bpy.context.scene
scene.objects.link(object)
object.select = True
```

This snippet   
- adds a new empty mesh called 'Base_Data' to the `bpy.data` collection.
- pushes `Verts, Edges, and an empty list` onto the new empty Mesh
    - The empty list `[]` is because `from_pydata` expects 3 arguments, none are optional
    - You can choose to pass just verts, or just verts+edges or just verts+faces like:  

    ```python
    mesh.from_pydata(Verts, [], [])
    mesh.from_pydata(Verts, Edges, [])
    mesh.from_pydata(Verts, [], Faces)
    ```
    
    - In the event you want to add some faces and some edges you can of course do
          mesh.from_pydata(Verts, Edges, Faces)
        



### sequentially adding vertices/edges/faces
______



### Not an empty Mesh?

There's no neat way to remove all vert/edges/faces data from an existing mesh without