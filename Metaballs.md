If you need to use metaballs, they recently (October 2015) got approx 10 fold speed increase! 

See this [blender.stackexchange.com](http://blender.stackexchange.com/questions/1349/scripting-metaballs-with-negative-influence) question that spawned this example. There's also more information given by various authors. The snippet below covers the basics that might otherwise not be obvious.

```python
import bpy

scene = bpy.context.scene

# add metaball object
mball = bpy.data.metaballs.new("MyBall")
obj = bpy.data.objects.new("MyBallObject", mball)
scene.objects.link(obj)

# test with different values, for viewport do you need ultra high res?
mball.resolution = 0.16  # View resolution
# mball.render_resolution = you decide

# first metaball element doesn't exist yet - create it.
ele = mball.elements.new()
ele.co = (0.0, 0.0, 0.0)
ele.use_negative = False
ele.radius = 2.0

# adding extra metaball elements to the object 
ele = mball.elements.new()
ele.co = (-0.726, 1.006, 0.559)
ele.use_negative = True
ele.radius = 0.82279
```