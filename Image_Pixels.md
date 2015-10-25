Blender comes with numpy built in. yep!

### Mix 3 images

```python
import math
import numpy as np
import bpy

def np_array_from_image(img_name):
    img = bpy.data.images[img_name]
    return np.array(img.pixels[:])

pixelsA = np_array_from_image('A')
pixelsB = np_array_from_image('B')
pixelsC = np_array_from_image('C')
pixelsD = (pixelsA + pixelsB + pixelsC) / 3

image_D = bpy.data.images['D']
image_D.pixels = pixelsD.tolist()

# then click in the UV editor / to update the view..to see the pixels of `D` updated
```

![imge](http://i.stack.imgur.com/rN8tP.png)

### Add smallest of each array
```python
# add smallest element values
interim_1 = np.minimum(pixelsA, pixelsB)
pixelsD = np.minimum(interim_1, pixelsC)
```

[img2](http://i.stack.imgur.com/4Jf9H.png)
