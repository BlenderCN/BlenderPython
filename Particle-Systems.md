    # make a plane
    bpy.ops.mesh.primitive_plane_add(radius=0.5)
    plane = bpy.context.active_object

    # add particle system to original object
    ps = original_obj.modifiers.new("grid particles", type='PARTICLE_SYSTEM')
    psettings = ps.particle_system.settings

    # particle settings
    psettings.distribution = 'GRID'
    psettings.emit_from = 'FACES'
    psettings.physics_type = 'NONE'
    psettings.grid_resolution = numdiv_shortest_side
    psettings.use_render_emitter = True
    psettings.show_unborn = True
    psettings.use_scale_dupli = True
    psettings.particle_size = 1.0
    psettings.render_type = 'OBJECT'
    psettings.dupli_object = plane