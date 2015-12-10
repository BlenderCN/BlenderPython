Blender bpy has a solid collection of methods to perform common geometric tasks, the mathutils.geometry submodule is worth exploring.

Example 1. intersect_line_plane

```python
import bpy
import bmesh
import mathutils

def extend_vertex(limit_axis='x', coordinate=4.2, system='local'):

    obj = bpy.context.edit_object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)
    verts = bm.verts
    try:
        v1, v2 = [v for v in bm.verts if v.select]
    except:
        print('need two vertices selected, or one edge')
        bm.free()
        return

    plane_idx = {'x': 0, 'y': 1, 'z': 2}.get(limit_axis)
    plane_co, plane_no = [0,0,0], [0,0,0]
    plane_no[plane_idx] = 1
    plane_co[plane_idx] = coordinate

    intersect_l_p = mathutils.geometry.intersect_line_plane
    
    if system == 'local':
        new_co = intersect_l_p(v1.co, v2.co, plane_co, plane_no, False)
        A_len = (v1.co-new_co).length
        B_len = (v2.co-new_co).length
    else:
        mw = obj.matrix_world
        new_co = intersect_l_p(mw * v1.co, mw * v2.co, plane_co, plane_no, False)
        A_len = ((mw*v1.co)-new_co).length
        B_len = ((mw*v2.co)-new_co).length
        new_co = mw.inverted() * new_co
        
    if A_len < B_len:
        v1.co = new_co
    else:
        v2.co = new_co

    bmesh.update_edit_mesh(me, True)


extend_vertex(limit_axis='x', coordinate=-2, system='global')
```