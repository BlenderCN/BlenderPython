disambiguation : Font object

### Text DataBlock (text files inside Blender)

Text data-blocks are used for all kinds of things.  Storing

- notes  
- scripts
- data (coordinates, data structures, relationships, etc.,)
- Any string.

### Creating a new text block with content

```python
some_str = "Hello\nMy name is\ngobbledigook"
f = bpy.data.texts.new('new_text.txt')
f.from_string(some_str)
```