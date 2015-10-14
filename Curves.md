### 2D

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
            polyline.points[num].co = cList[num][0], cList[num][1], 0, w

        polyline.order_u = len(polyline.points)-1
        polyline.use_endpoint_u = True
        polyline.use_cyclic_u = True


vectors = [
    [[0,0], [10,0], [10,10], [0,10], [0,0]], 
    [[1,1], [1,2], [2,2], [2,1], [1,1]]
]
MakeFilledPolyLine("NameOfMyCurveObject", "NameOfMyCurve", vectors)
```