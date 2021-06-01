# Pykivdroid
pykivdroid is a python module to control android

### Requirements
  kivy,android,pyjnius
  

### Introduction
```
     pykivdroid is python module to control Android.
      

```
#### Orientation
```python
from pykivdroid import orientation
#To get current orientation
a=orientation.get_orientation()
print(a)

#To set orientation 
#you can set any mode 'user','portrait','landscape' etc
orientation.set_orientation(mode='user')

```
   
