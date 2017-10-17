> TODO: show foreach_set for curve data

Blender has two main type of Curve types. 2D and 3D - and both have a variety of Spline types. Maybe this doesn't mean much to you if you haven't used Blender's Curves much, but it will be apparent after a bit of experimentation.

Available Spline types: `('POLY', 'BEZIER', 'BSPLINE', 'CARDINAL', 'NURBS')`. Each of these types expects its coordinate information in a different way. 

  - POLY:  Like a poly line, not smoothed, just a line between each coordinate.
  - NURBS: Smoothed lines between coordinates.
  - BEZIER: takes a collection Knots and Handles.
  - CARDINAL: ...
  - BSPLINE: ...

Sometimes the distinction between 2D and 3D is arbitrary, sometimes you can switch the Curve type to either, it depends on what you need.

### 2D (Polyline)

This snippet lets you create a 2d surface Curve. Think of this as a Filled Polyline. You can pass it any number of sublists and the function will deal with the sublists. If the sublists fall within the perimeter of the largest sublist then it will make holes. Try it.

```python
import bpy  

# weight  
w = 1 

def MakeFilledPolyLine(objname, curvename, cLists):
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')  
    curvedata.dimensions = '2D'  

    odata = bpy.data.objects.new(objname, curvedata)  
    odata.location = (0,0,0) # object origin  
    bpy.context.scene.objects.link(odata)  

    for cList in cLists:
        polyline = curvedata.splines.new('POLY')  
        polyline.points.add(len(cList)-1)  
        for num in range(len(cList)):
            # --------------------- = x            , y            , z, w   
            polyline.points[num].co = cList[num][0], cList[num][1], 0, w

        polyline.order_u = len(polyline.points)-1
        polyline.use_endpoint_u = True
        polyline.use_cyclic_u = True  # this closes each loop


vectors = [
    [[0,0], [10,0], [10,10], [0,10]], 
    [[1,1], [1,2], [2,2], [2,1]]
]
MakeFilledPolyLine("NameOfMyCurveObject", "NameOfMyCurve", vectors)
```

makes this:  
![image1](http://i.stack.imgur.com/TuxNP.png)


### 2D (Lettertype, Bezier)

It helps to see an example with Curves using Beziers and holes.
```python
import bpy    
from mathutils import Vector    


coordinates = [
    ((-1, 0, 0), (-0.7, 0, 0), (-1, 0.5521, 0)),
    ((0, 1, 0), (-0.5521, 1, 0), (0, 0.7, 0)),
    ((0, 0, 0), (0, 0.3, 0), (-0.3, 0, 0))
]

    
def MakeCurveQuarter(objname, curvename, cList, origin=(0,0,0)):    
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')    
    curvedata.dimensions = '2D'    
    
    objectdata = bpy.data.objects.new(objname, curvedata)    
    objectdata.location = origin
    
    bpy.context.scene.objects.link(objectdata)    
    
    polyline = curvedata.splines.new('BEZIER')    
    polyline.bezier_points.add(len(cList)-1)    

    for idx, (knot, h1, h2) in enumerate(cList):
        point = polyline.bezier_points[idx]
        point.co = knot
        point.handle_left = h1
        point.handle_right = h2
        point.handle_left_type = 'FREE'
        point.handle_right_type = 'FREE'

    polyline.use_cyclic_u = True    
    
MakeCurveQuarter("NameOfMyCurveObject", "NameOfMyCurve", coordinates)  
```

![img4](https://cloud.githubusercontent.com/assets/619340/10614751/41090bfe-775c-11e5-9e72-c33e580512dd.png)


### 3D (smooth path)

```python
import bpy  
import math
from math import cos, sin, pi
from mathutils import Vector  

tau = 2 * pi
w = 1 

num_points = 30
amp = lambda i: 5 if (i % 2) else 7
pos = lambda f, i: f(i/num_points*tau) * amp(i)
listOfVectors = [(pos(sin, i), pos(cos, i), 0) for i in range(num_points)]  
  
def MakePolyLine(objname, curvename, cList):  
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')  
    curvedata.dimensions = '3D'  
  
    objectdata = bpy.data.objects.new(objname, curvedata)  
    objectdata.location = (0, 0, 0)
    bpy.context.scene.objects.link(objectdata)  
  
    polyline = curvedata.splines.new('NURBS')  
    polyline.points.add(len(cList)-1)  
    for num in range(len(cList)):  
        polyline.points[num].co = (cList[num])+(w,)  
  
    polyline.order_u = len(polyline.points)-1
    polyline.use_endpoint_u = True
    polyline.use_cyclic_u = True    
    
  
MakePolyLine("NameOfMyCurveObject", "NameOfMyCurve", listOfVectors)
```
![image2](https://cloud.githubusercontent.com/assets/619340/10515857/abf5258e-7355-11e5-8193-faa6af1f6fa6.png)