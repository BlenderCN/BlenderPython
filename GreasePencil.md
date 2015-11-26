resources which cover this:  
- [query-grease-pencil-strokes-from-python](http://blender.stackexchange.com/questions/24694/query-grease-pencil-strokes-from-python)  
- [convert-curves-to-grease-pencil](http://blender.stackexchange.com/questions/36140/convert-curves-to-grease-pencil)  

### drawing trigonometry using Grease Pencil.

```python
import math
import bpy


def get_layer(gdata_owner, layer_name):

    grease_data = bpy.data.grease_pencil
    if gdata_owner not in grease_data:
        gp = grease_data.new(gdata_owner)
    else:
        gp = grease_data[gdata_owner]

    # get grease pencil layer
    if not (layer_name in gp.layers):
        layer = gp.layers.new(layer_name)
        layer.frames.new(1)
        layer.line_width = 1
    else:
        layer = gp.layers[layer_name]
        layer.frames[0].clear()

    return layer


def generate_gp3d_stroke(layer):
    layer.show_points = True
    layer.color = (0.2, 0.90, .2)
    s = layer.frames[0].strokes.new()
    s.draw_mode = '3DSPACE'  # or '2DSPACE'

    chain = []
    num_verts = 10
    r = 2.2
    gamma = 2 * math.pi / num_verts
    for i in range(num_verts+1):
        theta = gamma * i
        world_point = (math.sin(theta) * r, math.cos(theta) * r, 1.2)
        chain.append(world_point)

    s.points.add(len(chain))
    for idx, p in enumerate(chain):
        s.points[idx].co = p
        # s.points[idx].pressure = 1.0   # if 2DSPACE


class TrigGenerator(bpy.types.Operator):

    bl_idname = 'mesh.trig_generator'
    bl_label = 'generated trig with gpencil'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = bpy.context.object
        data_name = 'stack_data'
        layer_name = "stack layer"
        layer = get_layer(data_name, layer_name)
        generate_gp3d_stroke(layer)
        context.scene.grease_pencil = bpy.data.grease_pencil[data_name]
        return {'FINISHED'}


def register():
    bpy.utils.register_class(TrigGenerator)


def unregister():
    bpy.utils.unregister_class(TrigGenerator)


if __name__ == '__main__':
    register()
```

### Font to grease pencil.

Note, this fails a little bit (at present) because the polygons are filled using triangle fan, they aren't ngons like in bmesh.

```python
import bpy

def get_layer(gdata_owner, layer_name):

    grease_data = bpy.data.grease_pencil
    if gdata_owner not in grease_data:
        gp = grease_data.new(gdata_owner)
    else:
        gp = grease_data[gdata_owner]

    # get grease pencil layer
    if not (layer_name in gp.layers):
        layer = gp.layers.new(layer_name)
        layer.frames.new(1)
        layer.line_width = 1
    else:
        layer = gp.layers[layer_name]
        layer.frames[0].clear()

    return layer

def generate_gp3d_stroke(obj, layer):
    layer.show_points = True
    layer.color = (0.2, 0.90, .2)

    verts = obj.data.vertices
    for f in obj.data.polygons:

        s = layer.frames[0].strokes.new()
        s.draw_mode = '3DSPACE'  # or '2DSPACE'
        s.points.add(len(f.vertices))
        for i, v in enumerate(f.vertices):
            p = s.points[i]
            p.co = verts[v].co
            p.pressure = 1.0

def main():
    obj = bpy.context.active_object
    data_name, layer_name = 'stack_data', "stack layer"
    layer = get_layer(data_name, layer_name)
    generate_gp3d_stroke(obj, layer)
    bpy.context.scene.grease_pencil = bpy.data.grease_pencil[data_name]

main()
```

A small change should be to trianglulate or Quad the mesh first. ..

