Properties are what addons and operators use internally and on their UI. They are variables with potential side effects. An important feature of a property is they can call functions when their value is changed. To show what I mean let's take an abstract look.

```python
import bpy
from bpy.props import IntProperty
```
There are many more property types but the `IntProperty` is a convenient example. Take this hypothetical non-functioning piece of code

### Update function

The panel code for this can be found in _TextEditors -> Templates -> Python -> UI Panel Simple_.

```python
import bpy
from bpy.props import IntProperty


def my_update(self, context):
   print(self.some_int)

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.prop(context.scene, 'some_int')


def register():
    bpy.types.Scene.some_int = IntProperty(min=0, max=4, update=my_update)
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    del bpy.types.Scene.some_int


if __name__ == "__main__":
    register()

```
If you run the above code in TextEditor, it will add a panel to the Properties window, in the Scene Tab. It will look something like this:

![image](https://cloud.githubusercontent.com/assets/619340/11906029/106cc8b8-a5ca-11e5-9b15-25dbad98453d.png)

It will also print the current value of `some_int` to the console when you change it. It does this because of the update function, it calls `some_update()` with `self, context` being provided for us. Inside the `some_update()` function we are printing `self.some_int`, and self in this case is the same as `bpy.context.scene`. But.. we don't know from the update function which Property was modified to trigger it. Don't let this side track you - There's a solution.

### Update function defined inline using lambda

Now! let's say we want to do more dynamic stuff and want to know where the update came from. The update function can be defined _inline_.

```python
import bpy
from bpy.props import IntProperty


def my_update(self, context, origin):
   print(origin, getattr(self, origin))

class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    def draw(self, context):
        layout = self.layout
        obj = context.object
        col = layout.column()
        col.prop(context.scene, 'some_int')
        col.prop(context.scene, 'some_other_int')        


def register():
    bpy.types.Scene.some_int = IntProperty(
        min=0,
        update=lambda self, context: my_update(self, context, origin='some_int')
    )

    bpy.types.Scene.some_other_int = IntProperty(
        min=0,
        update=lambda self, context: my_update(self, context, origin='some_other_int')
    )

    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    del bpy.types.Scene.some_int
    del bpy.types.Scene.some_other_int    


if __name__ == "__main__":
    register()

```

### Organizing properties (avoid namespace pollution)

What's namespace pollution? It's like a classroom with 20 people, 6 of which are called Peter. Too much confusion regarding who's who - You need to ask their surnames to distinguish one from the other. This is called  'disambiguation'.. 

### Property Group / Pointer Property

```python
import bpy

## some panel somewhere
def draw(self, context):
    self.layout.prop(context.scene.my_prop_grp, 'custom_1')


class MyPropertyGroup(bpy.types.PropertyGroup):
    custom_1 = bpy.props.FloatProperty(name="My Float")
    custom_2 = bpy.props.IntProperty(name="My Int")

def register():
    bpy.utils.register_class(MyPropertyGroup)
    bpy.types.Scene.my_prop_grp = bpy.props.PointerProperty(type=MyPropertyGroup)

def unregister():
    bpy.utils.unregister_class(MyPropertyGroup)

    # deleting the group, removes automatically all children. :)
    del bpy.types.Scene.my_prop_grp


```

or like this.. 

```python
class SomeAddonProperties(bpy.types.PropertyGroup):

    @classmethod
    def register(cls):
        Scn = bpy.types.Scene

        Scn.some_addon_props = PointerProperty(
            name="some addon's internal global properties",
            description="some add-on uses these properties for shared properties between operators",
            type=cls,
        )

        cls.custom_1 = bpy.props.FloatProperty(name="My Float")
        cls.custom_2 = bpy.props.IntProperty(name="My Int")


    @classmethod
    def unregister(cls):
        del bpy.types.Scene.some_addon_props


def register():
    ...
    bpy.utils.register_class(SomeAddonProperties)

def unregister():
    ...
    bpy.utils.unregister_class(SomeAddonProperties)   
```


### Iterating over a PropertyGroup (for use in UI for example)

for UI you really want to do this inline to avoid extra function calls.

```python
# imagine we have a PropertyGroup registered on bpy.types.Object
# and called it `parametric_circle`

props = obj.parametric_circle:
col = l.column()
for propname in props.rna_type.properties.keys():
    if propname in {'rna_type', 'name'}:
        continue
    col.prop(props, propname)
```

but for one off lookups, it might be nice to have a helper function:

```python
def get_props2(consumable):
    propnames = consumable.rna_type.properties.keys()
    for p in filter(lambda n: not n in {'rna_type', 'name'}, propnames):
        yield p

# usage..
obj = bpy.context.active_object
for i in get_props2(obj.parametric_circle):
    print(i)
```

### Storing / Importing properties as json or dictionary literal

Also known as serialization / deserialization. Code for that can be found here: [reading-and-writing-json-or-dict-literal](bpy_data_texts#reading-and-writing-json-or-dict-literal)