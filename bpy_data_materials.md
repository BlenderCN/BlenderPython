Cycles Materials (Nodes, no Nodes)  
Internal Materials (Nodes, no Nodes)  

## Cycles Materials - scripted

### Node Groups

Perhaps you want to manually define materials and node groups, and import ('append') them from another `.blend` via a script.
```python
todo

```

### Nodes

Scripting the generation of a Cycles node tree is quite easy. The only thing I find moderately annoying is also passing the locations of the nodes (if you don't pass locations all nodes are added to (x=0, y=0)). 




**NodeArrange to the rescue**  

Luckily there's a small [addon by JuhaW called NodeArrange](https://github.com/JuhaW/NodeArrange) that is able to spread the nodes out in a tree form.

```python
import bpy

import addon_utils
addon_utils.enable("NodeArrange-master")

mat = bpy.data.materials.new('Demo2')
mat.use_nodes = True
nodes = mat.node_tree.nodes 

# remove default diffuse node, get output node
nodes.remove(nodes.get('Diffuse BSDF'))
material_out = nodes.get('Material Output')

bsdf1 = nodes.new(type='ShaderNodeBsdfDiffuse')
bsdf1.inputs[0].default_value = 0, 0.2, 0.9, 1.0

bsdf2 = nodes.new(type='ShaderNodeBsdfDiffuse')
bsdf2.inputs[0].default_value = 0.8, 0.2, 0.9, 1.0

value1 = nodes.new(type='ShaderNodeValue')
mixer1 = nodes.new(type='ShaderNodeMixShader')

links = mat.node_tree.links
links.new(value1.outputs[0], mixer1.inputs[0])
links.new(bsdf1.outputs[0], mixer1.inputs[1])
links.new(bsdf2.outputs[0], mixer1.inputs[2])
links.new(mixer1.outputs[0], material_out.inputs[0])

bpy.ops.node.arrange_nodetree(mat_name=material_name)
or even

#bpy.ops.node.arrange_nodetree(
#  mat_name=material_name, margin_x=140, margin_y=120
#)
```

### No Nodes


