
bl_info = {
	"name": "cs name", #插件名字
	"author": "cs author",#作者名字
	"version": (9, 9, 9),#插件版本
	"blender": (9, 99, 0),#blender版本
	"location": "3DView > Tools",#插件所在位置
	"description": "Cha Jian cs???",#描述
	"warning": "xxx",#警告
	"wiki_url": "http://tieba.baidu.com/"
	"f?kw=黑猫鸣泣时&fr=index&red_tag=2858782483", #文档地址
	"support": 'OFFICIAL',#
	"category": "Mesh",#分类
}

import bpy

class H_class(bpy.types.Panel):
	"""Creates a Panel in the Object properties window"""
	bl_label = "菜单标题"
	bl_idname = "OBJECT_PT_hello"#未知 可以改
	bl_space_type = 'PROPERTIES' #枚举('EMPTY', 'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR', 'IMAGE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'TEXT_EDITOR', 'NODE_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINE)
	bl_region_type = 'WINDOW' #枚举 ('WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'PREVIEW')
	bl_context = "object" #未知 不可以改


def draw(self, context):
	layout = self.layout
	obj = context.object
	row = layout.row()
	row.label(text="文字1", icon='WORLD_DATA')
	row = layout.row()
	row.label(text="文字2" + obj.name)
	row = layout.row()
	row.prop(obj, "文字3")
	row = layout.row()
	row.operator("mesh.primitive_cube_add")


class panel_1(bpy.types.Panel): #物体属性面板
	"""Creates a Panel in the Object properties window"""
	bl_label = "菜单标题"
	bl_idname = "OBJECT_PT_hello"#未知 可以改
	bl_space_type = 'PROPERTIES' #枚举('EMPTY', 'VIEW_3D', 'TIMELINE', 'GRAPH_EDITOR', 'DOPESHEET_EDITOR', 'NLA_EDITOR',         'IMAGE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'TEXT_EDITOR', 'NODE_EDITOR', 'LOGIC_EDITOR', 'PROPERTIES', 'OUTLINE)
	bl_region_type = 'WINDOW' #枚举 ('WINDOW', 'HEADER', 'CHANNELS', 'TEMPORARY', 'UI', 'TOOLS', 'TOOL_PROPS', 'PREVIEW')
	bl_context = "object" #未知 不可以改


	def draw(self, context):
		layout = self.layout
		obj = context.object
		row = layout.row()
		row.label(text="文字1", icon='WORLD_DATA')
		row = layout.row()
		row.label(text="文字2" + obj.name)
		row = layout.row()
		row.prop(obj, "文字3")
		row = layout.row()
		row.operator("mesh.primitive_cube_add")


from bpy.types import Operator, Panel


class AddChain(bpy.types.Operator):
	"""Add a Chain"""
	bl_idname = "mesh.primitive_chain_add"
	bl_label = "Add Chain"
	bl_options = {'REGISTER', 'UNDO'}


	def execute(self, context): #点击按钮时候执行
		#Add_Chain()
		print("cs")
		return {'FINISHED'}


class panel_2(Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'Create'
	bl_label = "Add Chain"
	bl_context = "objectmode"
	bl_options = {'DEFAULT_CLOSED'}

	def draw(self, context):
		layout = self.layout
		layout.operator(AddChain.bl_idname, text="Chain")

class panel_2(bpy.types.Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = '标题' #标题名字
	bl_label = "测试" #菜单名字
	bl_context = "objectmode"
	bl_options = {'DEFAULT_CLOSED'}

	def draw(self, context):
		layout = self.layout
		layout.operator(AddChain.bl_idname, text="按钮") #按钮名字


class AddChain(bpy.types.Operator):
	"""提示信息"""
	bl_idname = "mesh.primitive_chain_add"
	bl_idname = "mesh.cs_add" # python 提示
	bl_label = "Add Chain"
	bl_category = '标题' #标题名字
	bl_label = "测试" #菜单名字
	bl_options = {'REGISTER', 'UNDO'}
	bl_options = {'DEFAULT_CLOSED'} # HIDE_HEADER 为隐藏菜单


def execute(self, context): #点击按钮时候执行
	cs()
	return {'FINISHED'}



def register(): #启用插件时候执行
	print('525495787')
	bpy.utils.register_class(H_class) #注册一个类
	bpy.utils.register_module(__name__) #大概是注册这个模块

def unregister(): #关闭插件时候执行
	print('ZX')
	bpy.utils.unregister_module(__name__) #大概是注销这个模块
	bpy.utils.unregister_class(H_class) #注销一个类


if __name__ == "__main__":
register()
