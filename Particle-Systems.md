```python
import bpy

def quantize(original_obj, numdiv_shortest_side):

    # make a plane
    bpy.ops.mesh.primitive_plane_add(radius=0.5)
    plane = bpy.context.active_object

    # add particle system to original object
    ps = original_obj.modifiers.new("grid particles", type='PARTICLE_SYSTEM')
    psettings = ps.particle_system.settings

    # particle settings
    psettings.distribution = 'GRID'
    psettings.emit_from = 'FACE'
    psettings.physics_type = 'NO'
    psettings.grid_resolution = numdiv_shortest_side
    psettings.use_render_emitter = True
    psettings.show_unborn = True
    psettings.use_scale_dupli = True
    psettings.particle_size = 1.0
    psettings.render_type = 'OBJECT'
    psettings.dupli_object = plane

    plane.select = False
    
    original_obj.select = True
    bpy.context.scene.objects.active = original_obj
    bpy.ops.object.duplicates_make_real()
    original_obj.hide = True
    original_obj.select = False
    
    bpy.ops.object.make_local(type='SELECT_OBDATA')

    # find first of the new objects, to join the rest onto
    joiner = None
    for obj in bpy.data.objects:
        if not obj in {plane, original_obj}:
            joiner = obj
            bpy.context.scene.objects.active = obj
            break
    
    bpy.ops.object.delete(use_global=False)

    
    # join, and remove doubles
    bpy.ops.object.join()
    # bpy.ops.mesh.remove_doubles()


numdiv_shortest_side = 21
original_obj = bpy.context.active_object
quantize(original_obj, numdiv_shortest_side)
```