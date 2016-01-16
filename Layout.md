The best introduction to UI layout and the templating system used by Blender is still the UI cookbook. There's no harm in showing more examples, especially concerning the draw function.

All examples will use the same template code, unless otherwise specified. Image should show you what's different and then the code will start to make more sense.

### Responsive layout

You can get more complex and entirely rearrange layouts depending how many pixels wide the UI panel is. Below this example will reset the percentage of the width that the arrow buttons should occupy when the user resizes the panel horizontally.

```python
import bpy

from bpy.props import *
from bpy.types import Operator, Panel

class LayoutDemoPanel(Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):

        layout = self.layout
        scene = context.scene

        w = context.area.width

        row = layout.row(align=True)
        pct = 0.5
        if w > 300:
            pct = 0.3
        elif w > 400:
            pct = 0.2
        elif w < 200:
            pct = 0.7
        split = row.split(percentage=pct)
        
        OP = "render.render"
        
        l_split = split.split()

        left_side = l_split.column()
        left_side.operator(OP, text='',  icon='RIGHTARROW_THIN')
        left_side.operator(OP, text='', icon='TRIA_LEFT')
        left_side.operator(OP, text='', icon='RIGHTARROW_THIN')

        mid_side = l_split.column()
        mid_side.operator(OP, text='', icon="TRIA_UP")
        # mid_side.operator(OP, text='', icon="DISCLOSURE_TRI_RIGHT")
        mid_side.label('')
        mid_side.operator(OP, text='', icon="TRIA_DOWN")     

        right_side = l_split.column()
        right_side.operator(OP, text='', icon='RIGHTARROW_THIN')
        right_side.operator(OP, text='', icon="TRIA_RIGHT")
        right_side.operator(OP, text='', icon='RIGHTARROW_THIN')

def register():
    bpy.utils.register_class(LayoutDemoPanel)

def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
```


