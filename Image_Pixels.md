Blender comes with numpy built in. yep!

```python
import math
import numpy as np
import bpy

def np_array_from_image(img_name):
    img = bpy.data.images[img_name]
    # width, height = img.size[:]
    return np.array(img.pixels[:])  # .reshape([height, width, 4])

pixelsA = np_array_from_image('A')
pixelsB = np_array_from_image('B')
pixelsC = np_array_from_image('C')
pixelsD = (pixelsA + pixelsB + pixelsC) / 3

image_D = bpy.data.images['D']
image_D.pixels = pixelsD.tolist()

# then click in the UV editor / to update the view..to see the pixels of `D` updated
```