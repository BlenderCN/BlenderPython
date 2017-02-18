## custom icons for EnumProperty

```python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>


bl_info = {
    "name": "ploot",
    "author": "zeffii (aka Dealga McArdle)",
    "version": (1, 3, 1),
    "blender": (2, 7, 7),
    "category": "Mesh",
    "location": "View3D > EditMode > (w) Specials"
}

import os
import bpy



icon_names = ['BIX', 'CCEN', 'E2F']
icon_collection  = {}
icon_dict = {}


class DudePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(context.scene, 'enumlumpa', text='')


def register_icons():
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")
    for icon_name in icon_names:
        pcoll.load(icon_name, os.path.join(icons_dir, icon_name + '.png'), 'IMAGE')

    icon_collection["main"] = pcoll


def unregister_icons():
    for pcoll in icon_collection.values():
        bpy.utils.previews.remove(pcoll)
    icon_collection.clear()


def register():
    register_icons()

    icon_dict.update({name: icon_collection["main"][name].icon_id for name in icon_names})
    bpy.types.Scene.enumlumpa = bpy.props.EnumProperty(
        default='BIX',
        items=[(name, name.title(), '', icon_dict.get(name), idx) for idx, name in enumerate(icon_names)]
    )
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)
    unregister_icons()
    del bpy.types.Scene.enumlumpa

```