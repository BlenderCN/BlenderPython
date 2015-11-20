Most of the useful information about Operators can be acquired by taking your time to read through the add-on list. It's how I learnt it. My favorite snippets i've worked into a [sublime text editor autocomplete snippet set](https://github.com/zeffii/BlenderSublimeSnippets). The [bpy docs also cover](http://www.blender.org/api/blender_python_api_current/info_quickstart.html?highlight=operator) the various forms of `Operators` in some detail.  
  
My favorite things about the API might be worth explicitly mentioning. 

### Registration

If you have an addon / script with one class (Panel, Operator..etc.), you might register/unregister it using this. 
```python
def register():
    bpy.utils.register_class(YourClassName)

def unregister():
    bpy.utils.unregister_class(YourClassName)
```

As your add-on becomes more complex you'll want to register more than 1 class, but you probably don't want to be explicit about the class name for each new class. You can avoid writing code like this.

```python
def register():
    bpy.utils.register_class(ClassNameOne)
    bpy.utils.register_class(ClassNameTwo)
    bpy.utils.register_class(ClassNameThree)

def unregister():
    bpy.utils.unregister_class(ClassNameOne)
    bpy.utils.unregister_class(ClassNameTwo)
    bpy.utils.unregister_class(ClassNameThree)

```

Instead you can write something much shorter. This registers all `bpy` classes in the order that they appear in the file.

```python
def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
```

### Callbacks.

When we don't want to write a Class for each Operator, we can write a _delegation class_. Where the `execute` function behaves differently depending on some variable that was passed. 

```python
def function_one():
	...

def function_two():
	...

def function_three():
	...


class SomeReusableOperator(bpy.types.Operator):

    bl_idname = "wm.some_reusable_op"
    bl_label = "Short Name"

    fn_name = bpy.props.StringProperty(default='')

    def execute(self, context):
        exec(self.fn_name + '()')
        return {'FINISHED'}


# in your ui layout draw code somewhere

    callback = "wm.some_reusable_op"
    col.operator(callback, text='function one').fn_name = 'function_one'
    col.operator(callback, text='function two').fn_name = 'function_two'
    col.operator(callback, text='function three').fn_name = 'function_three'

```
You don't need to use `exec()` in the execute function, for dynamic programming you have many options. Another is finding the function within `globals()`:

```python
    def execute(self, context):
        # self.fn_name stores the string name of the function
        # take from globals, the function named the same as self.fn_name
        globals()[self.fn_name]()
```
using a full if-else would work too.. but do you need to? maybe you do, maybe you don't. 

```python
    def execute(self, context):
        if self.fn_name == 'function_one':
            function_one()
        elif self.fn_name == 'function_two':
            function_two()
        elif self.fn_name == 'function_three':
            function_three()
        return {'FINISHED'}
```

Maybe your functions take arguments. Your delegation class can have multiple properties besides `StringProperty`. Imagine the following

```python

def function_one(): return None
def function_two(): return None
def function_three(): return None
def function_four(): return None

def function_five(a, b):
    print(a + b)


class SomeReusableOperator(bpy.types.Operator):

    bl_idname = "wm.some_reusable_op"
    bl_label = "Short Name"

    param1 = bpy.props.IntProperty(default=20)
    param2 = bpy.props.IntProperty(default=20)
    fn_name = bpy.props.StringProperty(default='')

    def execute(self, context):
        if self.fn_name == 'function_five':
            function_five(param1, param2)
        else:
            exec(self.fn_name + '()')
        return {'FINISHED'}
```
The ui code to set the operator would then look like

```python
    callback = "wm.some_reusable_op"
    ...
    ...
    op_five = col.operator(callback, text='function five')
    op_five.fn_name = 'function_five'
    op_five.param1 = 30
    op_five.param2 = 25
```
You might not want to hardcode param1 and param2 (but sometimes that's exactly what you want). For dynamic properties accessed via a Panel you need to register them as scene properties

```python
    scn = bpy.contex.scene
    callback = "wm.some_reusable_op"
    ...
    ...
    col.prop(scn, 'scene_param_1', text='param 1')
    col.prop(scn, 'scene_param_2', text='param 2')
    op_five = col.operator(callback, text='function five')
    op_five.fn_name = 'function_five'
    op_five.param1 = scn.scene_param_1
    op_five.param2 = scn.scene_param_2


# in your register / unregister functions (never forget to unregister too)

def register():
    ...
    bpy.types.Scene.scene_param_1 = IntProperty()
    bpy.types.Scene.scene_param_2 = IntProperty()

def register():
    ...
    del bpy.types.Scene.scene_param_1
    del bpy.types.Scene.scene_param_2
```

