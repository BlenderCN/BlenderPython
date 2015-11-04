More examples of parenting, with (respect to dupliverts / duplifaces)[Duplication]. 

If you want to parent one object to another, don't use `bpy.ops`, use the `.parent` attribute instead. For example if you have a Cube and want it to be the parent of a Sphere.

```python
objects = bpy.data.objects
cube = objects['Cube']
sphere = object['Sphere']
sphere.parent = cube
```

