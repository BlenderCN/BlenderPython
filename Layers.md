Moving objects that appear in one range of layers, to another range.

```python
import bpy

for obj in bpy.data.objects:
    
    # let's deal with a simple case: is it only on one layer?
    if obj.layers[:].count(True) == 1:
        found_index = obj.layers[:].index(True)
        if (5 <= found_index <= 10):
            new_index = found_index + 5
            obj.layers[:] = [i==new_index for i in range(20)]
```

Here restated with a new function called `set_layer`, to encapsulate the behavior. It's less efficient, but arguably easier to read.


```python
import bpy

def set_layer(obj, idx):
    obj.layers[:] = [i==idx for i in range(20)]

for obj in bpy.data.objects:
    if obj.layers[:].count(True) == 1:
        found_index = obj.layers[:].index(True)
        if found_index in {5,6,7,8,9}:
            set_layer(obj, found_index + 5)
```

Here's an alternative, which might be interesting if you're new to python

```python
import bpy

only_on_one_layer = lambda o: o.layers[:].count(True) == 1

for o in filter(only_on_one_layer, bpy.data.objects):
    layer_id = o.layers[:].index(True)
    if layer_id in {5,6,7,8,9}:
        o.layers[:] = [i == (layer_id + 5) for i in range(20)]
```