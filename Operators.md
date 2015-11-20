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
You don't need to use `exec()` in the executure, using a full if-else would work too.. but do you need to?

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