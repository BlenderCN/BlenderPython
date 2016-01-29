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

print('--')

for prop in get_props2(f):
    value = getattr(f, prop)
    
    try:
        can_iterate = iter(value)
        print(prop, value[:])
    except TypeError:
        if prop == 'space':
            print(prop)
        else:
            print(prop, value)

        
    # print(type(value))
```
### brutal exporter for 3dview theme

```python
import bpy
import json

def get_props2(consumable):
    propnames = consumable.rna_type.properties.keys()
    for p in filter(lambda n: not n in {'rna_type', 'name'}, propnames):
        yield p

current_theme = bpy.context.user_preferences.themes.items()[0][0]  
view = bpy.context.user_preferences.themes[current_theme].view_3d

print('--')
theme_dict = {}

for prop in get_props2(view):
    value = getattr(view, prop)
    
    try:
        can_iterate = iter(value)
        # print(prop, value[:])
        theme_dict[prop] = [round(v, 5) for v in value[:]]
    except TypeError:
        
        # skip for now..
        if prop == 'space':
            space = getattr(view, prop)
            # print(prop, dir(space))
        else:
            # print(prop, value)
            theme_dict[prop] = value

texts = bpy.data.texts
# dump string
m = json.dumps(theme_dict, sort_keys=True, indent=2)
theme_file_name = 'my_theme.json'

text_block = texts.get(theme_file_name)
if not text_block:
    text_block = texts.new(theme_file_name)

text_block.from_string(m)
```    


