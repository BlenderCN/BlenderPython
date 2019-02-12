import bpy


class LayoutDemoPanel(bpy.types.Panel): #物体属性面板
    """Creates a Panel in the scene context of the properties editor
    https://docs.blender.org/api/blender_python_api_2_76_release/bpy.types.Panel.html
    """
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES' # 枚举('CLIP_EDITOR','CONSOLE','DOPESHEET_EDITOR','FILE_BROWSER','GRAPH_EDITOR','IMAGE_EDITOR','INFO','NLA_EDITOR','NODE_EDITOR','OUTLINER','PREFERENCES','PROPERTIES','SEQUENCE_EDITOR','STATUSBAR','TEXT_EDITOR','TOPBAR','VIEW3D_MT_editor_menus','VIEW_3D',)
    bl_region_type = 'WINDOW' # 面板所在区域,枚举 ('EXECUTE','HEADER','NAVIGATION_BAR','TOOL_PROPS','TOOLS','UI','WINDOW')
    bl_context = "scene" # 面板作用情境

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        layout.label(text=" Simple Row:")

        row = layout.row()
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create an row where the buttons are aligned to each other.
        layout.label(text=" Aligned Row:")

        row = layout.row(align=True)
        row.prop(scene, "frame_start")
        row.prop(scene, "frame_end")

        # Create two columns, by using a split layout.
        split = layout.split()

        # First column
        col = split.column()
        col.label(text="Column One:")
        col.prop(scene, "frame_end")
        col.prop(scene, "frame_start")

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Column Two:")
        col.prop(scene, "frame_start")
        col.prop(scene, "frame_end")

        # Big render button
        layout.label(text="Big Button:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("render.render")

        # Different sizes in a row
        layout.label(text="Different button sizes:")
        row = layout.row(align=True)
        row.operator("render.render")

        sub = row.row()
        sub.scale_x = 2.0
        sub.operator("render.render")

        row.operator("render.render")


def register():
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
