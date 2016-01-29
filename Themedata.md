I like to switch themes for taking screenshots vs doing longer modeling sessions.

This is definitely a work in progress. Especially 3dview has a number of settings that need special attention for a script to serialize and deserialize the state.

```python
import bpy


def get_props2(consumable):
    propnames = consumable.rna_type.properties.keys()
    for p in filter(lambda n: not n in {'rna_type', 'name'}, propnames):
        yield p

current_theme = bpy.context.user_preferences.themes.items()[0][0]  
f = bpy.context.user_preferences.themes[current_theme].view_3d

for prop in get_props2(f):
    value = getattr(f, prop)
    print(prop, str(value))
    # print(type(value))
```