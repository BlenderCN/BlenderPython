some assumptions about the whole thing:

- square image
- you use Meters of Blender Units. (Else the `texture_dpi` function changes a little)
- you pass the correct image name (or image of equivalent dimensions)
- you have an active uvmap
- you are in edit mode.

Insight can also be found at _TextEditor -> Templates -> Python -> Operator Mesh UV_

```python
import math

import bpy
import bmesh
from mathutils import Vector


def texture_dpi(polygon_area, uv_area, image_dim):
    """
    polygon_area:   in (meters or BU)
    uv_area:        in ratio (0..1)
    image_dim:      either width or height of image, this assumes
                    square images anyway, else none of this makes sense
    """

    l1 = math.sqrt(polygon_area)
    l2 = math.sqrt(uv_area)

    # assume the units are BU or meter.
    inches = l1 * 39.3701
    pixels = int(l2 * image_dim)
    return int(pixels / inches)


def calc_area_from_2d_vectorlist(v):
    # http://www.mathopenref.com/coordpolygonarea.html
    sum = 0
    n = len(v)
    for i in range(n - 1):
        sum += ((v[i].x * v[i + 1].y) - (v[i].y * v[i + 1].x))
    sum += ((v[n - 1].x * v[0].y) - (v[n - 1].y * v[0].x))
    return abs(sum / 2)


def get_bm_from_edit_object(image_name):
    obj = bpy.context.edit_object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    uv_layer = bm.loops.layers.uv.verify()
    bm.faces.layers.tex.verify()

    totals = []
    for f in bm.faces:
        vl = [l[uv_layer].uv for l in f.loops]
        fa = calc_area_from_2d_vectorlist(vl)  # 2d area of uv loop
        totals.append([f.calc_area(), fa])     # 2d area of face (local size)
        break  # if homogeneous  , else comment it out.

    image_dim = bpy.data.images[image_name].size[0]
    for polygon_area, uv_area in totals:
        dpi = texture_dpi(polygon_area, uv_area, image_dim)
        print(dpi)

get_bm_from_edit_object('some_texture.png')
```