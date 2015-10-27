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

You can execute this code with or without the line that modifies each vertices' normal.

```python


```

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

Reusing some of the code created for the [bmesh.ops wiki page](https://github.com/zeffii/BlenderPythonRecipes/wiki/bmesh_ops)

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

create_uv_sphere('my_uvsphere', u=5, v=4, d=1)
```