# Pykivdroid
pykivdroid is a python module to control android

### Requirements
  kivy,android,pyjnius
  

### Introduction
```
     pykivdroid is python module to control Android.
     To test all this things you have to use android device.
```
      
#### Installation
```
  In buildozer.spec file 
   requirements = python3,kivy==2.0.0,pyjnius,android,pykivdroid
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



### Text To Speech

```python
#permission INTERNET
from pykivdroid.tts import TTS
tts=TTS()
tts.speak('text to speak')
##see also and for more info see tts.py in pykivdroid.
tts.get_voices()
tts.get_language()
tts.get_engines()
tts.get_duration()
tts.get_available_languages()
tts.get_default_voice()
tts.get_max_input_length()
tts.get_default_engine()
tts.set_voice(voice)
tts.set_pitch(pitch)
tts.set_language(loc)
tts.set_speech_rate(rate)
tts.is_speaking()
tts.is_language_available(loc)

```


```python
#example with kivy
#permission INTERNET
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from pykivdroid.tts import TTS
from pykivdroid import ArrayList,Arrays


class MyApp(App):
    text='Python is good programming language'
    i=0
    def build(self):

        self.box=BoxLayout(orientation="vertical")

        self.ti=TextInput(text=self.text)

        #slider used to change pitch
        self.sldr=Slider(min=0,max=1,value=0.5)
        #slider used to change speech rate
        self.sldr2=Slider(min=0,max=1,value=0.5)
        #1)tts object
        self.tts=TTS()
        
        #self.voice=self.tts.get_voices()

    
        self.box.add_widget(self.ti)
        self.box.add_widget(self.sldr)
        self.box.add_widget(self.sldr2)
        self.box.add_widget(Button(text='speak',on_release=self.callback))
        
        return self.box
    def callback(self,obj):
        #changing voice

        voice=self.tts.get_voices()
        
        if self.i==len(voice):
            self.i=0
        
        self.tts.set_voice(voice[self.i])

       
        
       
        
        self.tts.set_pitch(self.sldr.value)
        self.tts.set_speech_rate(self.sldr2.value)
        self.tts.speak(self.ti.text)
        #print(self.tts.get_voices())
        self.i+=1



   
MyApp().run()

```

#### Unity Ads
```
1)Download Unity-ads.aar from unity ads 
2)Creat libs folder in your project folder 
3)Add Unity-ads.aar to your /libs folder

update buildozer.spec 

android.add_aars = ./libs/*.aar
android permissions = INTERNET,ACCESS_NETWORK_STATE
```
[Unity-ads.aar download page ](https://github.com/Unity-Technologies/unity-ads-android/releases)

##### Unity Interstitial and Reward ads 
```python
'''

'''
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from pykivdroid.unityads import UnityHandler

class MyApp(App):
    def build(self):
        self.box=BoxLayout(orientation='vertical')
         #1 step 
        self.uh=UnityHandler(app_id='put app id here',)
         #2 set ads_type="reward" or "interstitial",test_mode=True or False,callback is used for Reward ads status for interstetial put callback=None
        self.uh.init_ads(ads_type="reward",test_mode=True,callback=self.call_status)

        self.box.add_widget(Button(text='show reward ads',on_release=self.call))
        return self.box

    def call(self,obj):
        self.uh.show_ads('put ads id here')

    def call_status(self,status):
        print("reward : ",status)


MyApp().run()

```
##### Unity Banner ads 
```  I have implemented unity banner ads but test mode is only working in India ```

[Banner ads issue](https://forum.unity.com/threads/could-not-show-banner-due-to-no-fill-for-placement.610948/)
```python
#simple example
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout
from pykivdroid.unityads import UnityHandler

class MyApp(App):
    def build(self):
        self.box=BoxLayout(orientation='vertical')
        self.uh=UnityHandler(app_id='put app id ',)
        #self.uh.init_ads(ads_type="reward",test_mode=False,callback=self.callback)
        self.uh.init_banner_ads('put ads id',test_mode=True,top_pos=True)
        self.uh.load_banner()

        

        self.box.add_widget(Button(text='show banner ads',on_release=self.call))
        self.box.add_widget(Button(text='hide banner ads  ',on_release=self.call2))
        return self.box
    def call2(self,obj):
        self.uh.hide_banner()

    def call(self,obj):
        
        self.uh.show_banner()
        self.uh.load_banner()

        #self.uh.show_ads()
    def callback(self,*a):
        print("hello",a)


MyApp().run()

```

