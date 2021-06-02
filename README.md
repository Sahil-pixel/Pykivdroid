# Pykivdroid
pykivdroid is a python module to control android

### Requirements
  kivy,android,pyjnius
  

### Introduction
```
     pykivdroid is python module to control Android.
     To test all this things you have to use android device.
      

```
#### Classes and mActivity
```python
# I have defined java android class 
# Camera = autoclass('android.hardware.Camera')
# And Nested class. N use to indicate nested 
# CameraNCameraInfo=autoclass('android.hardware.Camera$CameraInfo')
# mActivity is App's activity
from pykivdroid import mActivity,Camera,CameraNCameraInfo
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
from pykivdroid import brightness,write_settings
'''
Required Permissions:
    WRITE_SETTINGS
'''
#To get current brightness
a=brightness.get_brightness()
print(a)
#To set brightness
#minimum brightness is 0, maximum is 100
write_settings(sdk_int, version_code) #TO GET PERMISSION
brightness.set_brightness(50)
```
### Speech to text
```python
from pykivdroid.stt import STT
'''
     Android Permissions:INTERNET,RECORD_AUDIO
'''
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
### File Picker
```python
#Android permissions READ_EXTERNAL_STORAGE
from pykivdroid.picker import AndroidPicker
def callback(uri):
     print(uri)
ap=AndroidPicker(callback)
ap.pick_file(MIME_type='*/*')


```
```python 
####simple example
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pykivdroid.picker import AndroidPicker
from pykivdroid import request_permissions,Permission


class MyApp(App):
    def build(self):
        request_permissions([Permission.READ_EXTERNAL_STORAGE])
        self.box=BoxLayout(orientation="vertical")
        self.ap=AndroidPicker(self.call)
        self.ti=TextInput()
        self.box.add_widget(Button(text='OPEN AndroidPicker',on_release=self.callback))
        self.box.add_widget(self.ti)
        return self.box
    def callback(self,obj):
        self.ap.pick_file()

    def call(self,uri):
        print(uri)
        self.ti.text=str(uri)



MyApp().run()

```

### Android Video View
```python
from pykivdroid.videoview import AndroidVideoView

videoview=AndroidVideoView()

videoview.set_video_uri(uri)
#or
videoview.set_video_path(path)
#to start 
videoview.start()
#to seek any position
videoview.seek_to(ms)
#to stop
videoview.stop_playback()
#pause
videoview.pause()
#resume
videoview.resume()
#get duration
videoview.get_duration()
#get current position
videoview.get_current_position()
#to get audio session id 
videoview.get_audio_session_id()
#playing or not
print(videoview.is_playing())
######for more info. read videoview.py in pykivdroid 
```
```python
#simple example with kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pykivdroid.picker import AndroidPicker
from pykivdroid import request_permissions,Permission
from pykivdroid.videoview import AndroidVideoView


class MyApp(App):
    def build(self):
        request_permissions([Permission.READ_EXTERNAL_STORAGE])
        self.box=BoxLayout(orientation="vertical")
        self.ap=AndroidPicker(self.call)
        self.vv=AndroidVideoView()
        self.box.add_widget(self.vv)
        self.box.add_widget(Button(text='choose video',on_release=self.callback))
        
        return self.box
    def callback(self,obj):
        self.ap.pick_file()

    def call(self,uri):
        print(uri)
        self.vv.set_video_uri(uri)
        self.vv.start()



MyApp().run()

```
