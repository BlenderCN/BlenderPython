disambiguation : Font object

### Text DataBlock (text files inside Blender)
____
Text data-blocks are used for all kinds of things.  Storing

- notes  
- scripts
- data (coordinates, data structures, relationships, etc.,)
- Any string.

Creating a new text block with content is as simple as this:

```python
some_str = "Hello\nMy name is\ngobbledigook"
f = bpy.data.texts.new('new_text.txt')
f.from_string(some_str)
```

### reading and writing `json` or `dict literal`

Both methods below work only on dicts that can be stringified, so they can't contain Objects.

**json** 

A general Python solution to this involving JSON writing and reading. JSON can easily be constructed from a dictionary and written to `bpy.data.texts` as a string.

Imagine you have some dict of information, call it `my_dict`. To write that dict as a JSON to the .blend file you do:

```python
    import bpy
    import json
    
    my_dict = {
      'key1': 'some string storage',
      'key2': ['some', 'list', 'storage'],
      'key3': 5
    }
    
    # dump string
    m = json.dumps(my_dict, sort_keys=True, indent=2)
    text_block = bpy.data.texts.new('my_storage.json')
    text_block.from_string(m)
```

`bpy.data.texts['my_storage.json']` would then contain:

```python

    {
      "key1": "some string storage",
      "key2": [
        "some",
        "list",
        "storage"
      ],
      "key3": 5
    }
```
to read this back in at a later stage:

```python
    import bpy
    import json
    
    text_obj = bpy.data.texts['my_storage.json']
    text_str = text_obj.as_string()
    
    my_json = json.loads(text_str)
    print(my_json['key1'])

```


**dict and ast.literal_eval**  

```python
    import bpy
    import ast
    
    mydict = dict(deb=["two", "three"], far="booo", foo=34)
    
    # write the string representation of the dict to a text datablock
    # this assumes you know how to create text datablocks, it is shown in the other method anyway.
    d = bpy.data.texts['dict_storage']
    d.from_string(str(mydict))
    
    # read from the datablock
    d = bpy.data.texts['dict_storage']
    stringified_dict = d.as_string()
    my_read_dict = ast.literal_eval(stringified_dict)
    
    for k, v in my_read_dict.items():
        print(k, v)
```