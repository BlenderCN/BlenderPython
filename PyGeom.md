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
