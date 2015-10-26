October 2015  
  
This topic is something people tend to gravitate towards once they've grasped the notions of Meshes:  vertices, normals, indices, Vectors and Matrices - and the trigonometry and Linear Algebra used to perform calculations / transformations on them. This page will assume you are at that stage. Blender comes with many convenience functions to get you started.

Else there is [further reading](Further_Reading_LA) to accompany this if things aren't making sense.

2d text in the viewport is drawn using `blf` see below.

## BGL

This is a python wrapper around openGL drawing commands. openGL is a big topic, but once you understand the elementary concepts (which I intend to cover here) the learning curve for new openGL concepts gets less steep. It's possible to accomplish a lot without really knowing much about how openGL or the wrapper works.

You want to draw stuff. We could start with drawing 3d lines in the viewport with bgl, but Blender comes with a nice template to draw 2d lines. Let's start minimal.

_TextEditor -> Templates -> Python -> 3dView Modal Draw_



