The scenario to consider here is as follows: You need to render thousands of spheres and each sphere has a unique center coordinate. Creating thousands of spheres one Object at a time, even when scripted, is a bit slow and gets increasingly slower overall when you add more Objects. 

If you really want to know why that is , it's covered in this [BSE question / answer]()

Rather than creating thousands of unique Objects, which  

1. take up a lot of space in memory, and 
2. require name collision checking

### Dupliverts

It's possible to do this by making 2 objects.  

  - In words: 1 Sphere and 1 object with vertices at the locations where you want the spheres to be duplicated. 
  - In images: this tends to make immediate sense.


