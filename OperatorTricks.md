### reusing functions from other classes / operators

**One method**

Most of the time if I have functionality that is shared between Operators, I'll take them out of the class and reference them in the operators.

```python

def some_shared_function(caller, context):
    # ...
    return 

class A(bpy.types.Operator):
    (...)
    def execute(self,context):
        some_shared_function(self, context)

class B(bpy.types.Operator):
    (...)
    def execute(self,context):
        # other code here
        some_shared_function(self, context)

```

**Another method**  

Or make the operator behave differently depending on the passed parameters

```python
class AB(bpy.types.Operator):
    bl_idname = "wm.simple_multi_operator"
    bl_label = "Multi Purpose Operator"

    param_one = StringProperty()
    # param_two = StringProperty()

    def execute(self,context):

        if self.param_one == 'A':
        	self.some_functionality(context)

        elif self.param_one == 'B':
        	# some other code
        	self.some_functionality(context)

        return {'FINISHED'}

    def some_functionality(self, context):
    	...

```
   
in your ui code you'd pass parameters like this

```python

row = layout.row()
opname = "wm.simple_multi_operator"
row.operator(opname, text='A').param_one = 'A'
row.operator(opname, text='B').param_one = 'B'

# if you have more than one property for the operator
op_two = row.operator(opname, text='B / Mode Y')
op_two.param_one = 'B'
op_two.param_two = 'Mode Y'

```

calling the operator from a script directly works this way

```python
    
# or calling from a script
bpy.ops.wm.simple_multi_operator(param_one='A')
bpy.ops.wm.simple_multi_operator(param_one='B')

# with more than one parameter pass the keywords and values
bpy.ops.wm.simple_multi_operator(param_one='B', param_two='Mode Y')

```
There pros and cons with this method worth mentioning. 
  
- con: If you are in the habit of making tooltips for your Operators, this approach doesn't let you define a unique tooltip for the buttons.  
- pro: you can quickly give an Operator new functionality without declaring a whole new Operator  


**Aother method (using Python's classmethod decorator)**

```python
import bpy


class A(bpy.types.Operator):
    bl_idname = "object.simple_operator_a"
    bl_label = "Simple Object Operator A"
    
    def execute(self,context):
        self.some_function()
        return {'FINISHED'}
    
    @classmethod
    def some_function(cls, some_parameter='not woop'):
        print('some_parameter', some_parameter)

class B(bpy.types.Operator):
    bl_idname = "object.simple_operator_b"
    bl_label = "Simple Object Operator B"
        
    def execute(self,context):
        A.some_function('woooop')
        return {'FINISHED'}


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()

```

then calling them:

```python
>>> bpy.ops.object.simple_operator_a()
some_parameter not woop
{'FINISHED'}

>>> bpy.ops.object.simple_operator_b()
some_parameter woooop
{'FINISHED'}

```

Not sure if this is helpful, but adding for completeness:

```python
# autocomplete from the open parenthesis gives:
>>> bpy.types.OBJECT_OT_simple_operator_a.some_function(
some_function(cls, some_parameter='not woop')

# calling the function, gives:
>>> bpy.types.OBJECT_OT_simple_operator_a.some_function()
some_parameter not woop
```
