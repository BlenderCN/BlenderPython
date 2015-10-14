# Mesh

There are two ways to create `Mesh` data.  

- One relies on first defining all vertices / edges / faces in lists and then sending them to a function called `.from_pydata()`.
- The other grows the mesh in place by adding verts and indices sequentially.

Both methods have strengths and weaknesses, picking which to use depends largely on what you're doing.

### from_pydata

Date: Oktober 2015

This method expects the `Mesh` object to be empty (more about that below). 



### sequentially adding vertices/edges/faces




### Not an empty Mesh?

There's no neat way to remove all vert/edges/faces data from an existing mesh without