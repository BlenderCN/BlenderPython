This page is mostly a code dump and not arranged for convenient reading. sorry.

### Matrix Multiplication

matrix multiplication  , matrix in , vlist in
```python
def multiply_vectors(M, vlist):

    for i, v in enumerate(vlist):
        # write _in place_
        vlist[i] = (
            M[0][0]*v[0] + M[0][1]*v[1] + M[0][2]*v[2], 
            M[1][0]*v[0] + M[1][1]*v[1] + M[1][2]*v[2], 
            M[2][0]*v[0] + M[2][1]*v[1] + M[2][2]*v[2]
        )

    return vlist
```

### Closest point on triangle

from http://www.9math.com/book/projection-point-plane
closest point on a triangle , input ( point and 3points ) 
```python
def distance_point_on_tri(point, p1, p2, p3):
    n = obtain_normal3(p1, p2, p3)
    d = n[0]*p1[0] + n[1]*p1[1] + n[2]*p1[2]
    return abs(point[0]*n[0] + point[1]*n[1] + point[2]*n[2] + d) / sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2])
```
or easier to read..
```python
def distance_point_on_tri(point, p1, p2, p3):
    a, b, c = obtain_normal3(p1, p2, p3)
    x, y, z = p1  # pick any point of the triangle
    u, v, w = point
    d = a*x + b*y + c*z
    return abs(a*u + b*v + c*w + d) / sqrt(a*a + b*b + c*c)
```

### Unsorted

```python
import math

def interp_v3_v3v3(a, b, t=0.5):
    if t == 0.0: return a
    elif t == 1.0: return b
    else:
        s = 1.0 - t
        return (s * a[0] + t * b[0], s * a[1] + t * b[1], s * a[2] + t * b[2])

def length(v):
    return math.sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))

def normalize(v):
    l = math.sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))
    return [v[0]/l, v[1]/l, v[2]/l]

def sub_v3_v3v3(a, b):
    return a[0]-b[0], a[1]-b[1], a[2]-b[2]

def madd_v3_v3v3fl(a, b, f=1.0):
    return a[0]+b[0]*f, a[1]+b[1]*f, a[2]+b[2]*f

def dot_v3v3(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def isect_line_plane(l1, l2, plane_co, plane_no):
    u = l2[0]-l1[0], l2[1]-l1[1], l2[2]-l1[2]
    h = l1[0]-plane_co[0], l1[1]-plane_co[1], l1[2]-plane_co[2]
    dot = plane_no[0]*u[0] + plane_no[1]*u[1] + plane_no[2]*u[2]

    if abs(dot) > 1.0e-5:
        f = -(plane_no[0]*h[0] + plane_no[1]*h[1] + plane_no[2]*h[2]) / dot
        return l1[0]+u[0]*f, l1[1]+u[1]*f, l1[2]+u[2]*f        
    else:
        # parallel to plane
        return False

def obtain_normal3(p1, p2, p3):
    # http://stackoverflow.com/a/8135330/1243487
    return [
        ((p2[1]-p1[1])*(p3[2]-p1[2]))-((p2[2]-p1[2])*(p3[1]-p1[1])),
        ((p2[2]-p1[2])*(p3[0]-p1[0]))-((p2[0]-p1[0])*(p3[2]-p1[2])),
        ((p2[0]-p1[0])*(p3[1]-p1[1]))-((p2[1]-p1[1])*(p3[0]-p1[0]))
    ]

def mean(verts):
    vx, vy, vz = 0, 0, 0
    for v in verts:
        vx += v[0]
        vy += v[1]
        vz += v[2]
    numverts = len(verts) 
    return vx/numverts, vy/numverts, vz/numverts


def is_reasonably_opposite(n, normal_one):
    return dot_v3v3(normalized(n), normalized(normal_one)) < 0.0

```