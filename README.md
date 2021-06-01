# Pykivdroid
pykivdroid is a python module to control android

### Requirements
  kivy,android,pyjnius
  

### Introduction
```
     pykivdroid is python module to control Android.
     To test all this things you have to use android device.
      

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
   

#### Brightness
```python
from pykivdroid import brightness
#To get current brightness
a=brightness.get_brightness()
print(a)
#To set brightness
#minimum brightness is 0, maximum is 100
brightness.set_brightness(50)
```
### Speech to text
```python
from pykivdroid.stt import STT
###you can set language and mode offline or online 
sttobj=STT(language='en-US',prefer_offline=False)
#To start
sttobj.start()
#speech to text exsist or not 
a=sttobj.exist()
print(a)
#To stop
sttobj.stop()
#results
print(sttobj.results)
#partial
print(sttobj.partial)
#errors
print(sttobj.errors)
#listening or not
print(sttobj.listening)
#partial result
print(sttobj.partial_results)

```