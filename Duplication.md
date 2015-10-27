The scenario to consider here is as follows: You need to render thousands of spheres and each sphere has a unique center coordinate. Creating thousands of spheres one Object at a time, even when scripted, is a bit slow and becomes progressively slower the more objects you add.

If you really want to know why that is, it's covered in here:
  - [object-creation-slows-over-time](http://blender.stackexchange.com/questions/14814/object-creation-slows-over-time)  
  - [python-performance-with-blender-operators](http://blender.stackexchange.com/questions/7358/python-performance-with-blender-operators)  

Rather than creating thousands of unique Objects, which  

1. take up a lot of space in memory, and 
2. require name collision checking


### DupliVerts (duplication on vertices)
____
It's possible to do this by making 2 objects.  

  - In words: 
     - child: _1 Sphere_ 
     - parent: _1 vertex based mesh Object_ with vertices at the locations where you want the spheres to be duplicated. 
  - In images: this tends to make immediate sense.

Things to consider:  

- (pro) it is fast.  
- (pro) it is possible to rotate the object's vertex normals and use them as rotation values.  
- (con) vertex normals are overwritten by default when you enter edit mode of the parent object.  
- (con) no way to scale individual duplicates.  

Reusing code created for the [Mesh](Mesh) page, minus some comments. Read that link if you encounter problems.

You can execute this code with or without the last if statement. The last if statement shows how to switch on dupli vert rotation and how to set the normal of the vertices.

```python
import bpy
import bmesh
import math
import random


def create_cube(name, d=1, faces=True):
 
    Verts = [
        (1.0, 1.0, -1.0),
        (1.0, -1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (1.0, 1.0, 1.0),
        (1.0, -1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0)
    ]

    face_indices = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (4, 0, 3, 7)
    ]
     
    Faces = face_indices if faces else []

    if not (d == 1.0):
        Verts = [tuple(v*d for v in vert) for vert in Verts]

    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(Verts, [], Faces)
    mesh.update()

    obj = bpy.data.objects.new(name + "_Object", mesh)
    bpy.context.scene.objects.link(obj)  
    return obj


parent = create_cube('parent_cube', d=1, faces=False)
parent.dupli_type = 'VERTS'

child = create_cube('child_cube', d=0.2)
child.parent = parent

# let's rotate the vertex normals of the parent
parent.use_dupli_vertices_rotation = True
if (True):
    sin, cos = math.sin, math.cos
    for v in parent.data.vertices:
        rndx = random.random() * math.pi * 2
        rndy = random.random() * math.pi * 2
        rndz = random.random() * math.pi * 2
        v.normal = sin(rndx), cos(rndy), cos(rndy)


```
gets you something like this: all that's technically needed for the DupliVert is a _parent_ mesh Object containing verts, and of-course the child object.

![img dupliverts](https://cloud.githubusercontent.com/assets/619340/10757990/a6368996-7cae-11e5-8d61-b8908ca7b3ac.png)

### DupliFaces (duplication on faces)
____
very similar to DupliVerts, but this time it uses the face medians (think of average vertex) as duplication locations. 

Below - using a (parent) disjoint mesh of quads to duplicate the cone (child):   
![img face dupe](https://cloud.githubusercontent.com/assets/619340/10752213/72749cb4-7c87-11e5-9915-f435458937a3.png)

Things to consider:  

 - (pro) it is fast.  
 - (pro) Faces have a normal and that can be used as an orientation.  
 - (pro) Faces have an area, this can be used to scale the duplicates individually.  
 - (con) you have to create 3 or 4 vertices and corresponding face keys for your mesh for each desired duplicate. (This is a bit more work...it's not really a downside, but it needs to be mentioned).

The code: in order to demonstrate this using an object that has a good number of faces all pointing in different directions and all with different sizes. A UV Sphere. Here you'll notice the angles and scales of the duplicated object correspond to the face areas and face normals.

Reusing code created for the [bmesh.ops (primitives) page](https://github.com/zeffii/BlenderPythonRecipes/wiki/bmesh_ops_primitives), minus some comments. Read that link if you encounter problems.

```python
import bpy
import bmesh

def create_uv_sphere(name, u=5, v=4, d=1):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=u, v_segments=v, diameter=d)

    mesh = bpy.data.meshes.new(name + "_mesh")
    bm.to_mesh(mesh)
    bm.free()

    obj = bpy.data.objects.new(name, mesh)
    bpy.context.scene.objects.link(obj)
    return obj

parent = create_uv_sphere('parent_uvsphere', u=5, v=4, d=1)
child = create_uv_sphere('child_uvsphere', u=8, v=8, d=0.2)

child.parent = parent
parent.dupli_type = 'FACES'
parent.use_dupli_faces_scale = True

```
creates this:  
![image dupli-faces](https://cloud.githubusercontent.com/assets/619340/10755855/96c8a9f2-7ca0-11e5-8748-33b1b321130f.png)