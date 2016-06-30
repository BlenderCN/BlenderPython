stub:


This finds the largest open editor, splits it, then sets the editor type to for instance.. NODE_EDITOR.

```python
import bpy

def get_largest_area():
    window_reference = None
    surface_area = 0
    ctx = None
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            w, h = area.width, area.height 
            surface = w * h
            if surface > surface_area:
                surface_area = surface
                window_reference = area
                override = bpy.context.copy()
                override['area'] = area

    return window_reference, surface_area, override

area, size, ctx = get_largest_area()
bpy.ops.screen.area_split(ctx, direction='HORIZONTAL',factor=0.5)
bpy.ops.wm.context_set_string(ctx, data_path="area.type", value="NODE_EDITOR")
```