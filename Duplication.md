The scenario to consider here is as follows: You need to render thousands of spheres and each sphere has a unique center coordinate. Creating thousands of spheres one Object at a time, even when scripted, is a bit slow and gets increasingly slower overall when you add more Objects. 

If you really want to know why that is, it's covered in here:
  - [object-creation-slows-over-time](http://blender.stackexchange.com/questions/14814/object-creation-slows-over-time)  
  - [python-performance-with-blender-operators](http://blender.stackexchange.com/questions/7358/python-performance-with-blender-operators)  

Rather than creating thousands of unique Objects, which  

1. take up a lot of space in memory, and 
2. require name collision checking

### DupliVerts (duplication on vertices)

It's possible to do this by making 2 objects.  

  - In words: 
     - child: _1 Sphere_ 
     - parent: _1 vertex based mesh Object_ with vertices at the locations where you want the spheres to be duplicated. 
  - In images: this tends to make immediate sense.


> upside:
>   - it is fast, very fast.
>   - it is possible to rotate the object's vertex normals and use them as rotation values.
>
> Downside: 
>   - vertex normals are overwritten by default when you enter edit mode of the parent object.
>   - no way to scale individual duplicates.

### DupliFaces (duplication on faces)

very similar to DupliVerts, but this time instead of using vertices to give a duplication origin, it uses the face's median (think of average vertex). 

Below - using a (parent) disjoint mesh of quads to duplicate the cone (child):   
![img face dupe](https://cloud.githubusercontent.com/assets/619340/10752213/72749cb4-7c87-11e5-9915-f435458937a3.png)

> upside: 
> 
>  - it is fast
>  - Faces have a normal and that can be used as an orientation.
>  - Faces have an area, this can be used to scale the duplicates individually.  
>
> downside:  
>
>  - you have to create 3 or 4 vertices and corresponding face keys for your mesh. (This is a bit more work...it's not really a downside, but it needs to be mentioned)