from pykivdroid import TextToSpeech,ArrayList,Locale,mActivity,PythonJavaClass,\
java_method,sdk_int


'''
permission INTERNET
To get more info.
https://developer.android.com/reference/android/speech/tts/TextToSpeech#setOnUtteranceCompletedListener(android.speech.tts.TextToSpeech.OnUtteranceCompletedListener)
'''
#QUEUE_ADD
#QUEUE_FLUSH
class OnProgressListener(PythonJavaClass):
    __javainterfaces__ = ['android/speech/tts/UtteranceProgressListener']
    _callback=None
    def __init__(self,callback):
        super().__init__()
        self._callback=callback


    @java_method('(Ljava/lang/String;)V')
    def onStart(self,utteranceId):
        print("pykivdroid-----onStart")

    @java_method('(Ljava/lang/String;Z)V')
    def onStop(self,utteranceId,interrupted):
        print("pykivdroid-----onStop")

    @java_method('(Ljava/lang/String;III)V')
    def onRangeStart(self, utteranceId,  start,  end,  frame):
        print("pykivdroid-----onRANGESTART")




class TTS():
    def __init__(self,**kwargs):

        

        self._tts=TextToSpeech(mActivity,None)
        #if sdk_int>=15:
        #    obj=OnProgressListener(None)
        #self._tts.setOnUtteranceProgressListener(obj)

    def callback(self,x):
        print("id----",x)

    def speak(self,text,queue_mode=TextToSpeech.QUEUE_FLUSH,params=None):
        self._tts.speak(text,queue_mode,params)
    def set_language(self,loc):
        self._tts.setLanguage(loc)
    def set_pitch(self,pitch):
        self._tts.setPitch( pitch)
    def set_speech_rate(self,rate):
        self._tts.setSpeechRate(rate)
    def set_voice(self,voice):
        self._tts.setVoice(voice)
    def stop():
        self._tts.stop()
    def shutdown():
        self._tts.shutdown()
    def add_speech(self,text,uri):
        self._tts.addSpeech(text,uri)


    def get_available_languages(self):
    
    
        return self._tts.getAvailableLanguages().toArray()
        
        
    def get_default_engine(self):
        return  self._tts.getDefaultEngine()
    def get_default_language(self):
        return self._tts.getDefaultLanguage()
    def get_default_voice(self):
        return  self._tts.getDefaultVoice()
    def get_engines(self):
        return self._tts.getEngines()
    def get_language(self):
        return self._tts.getLanguage()
    def get_max_input_length(self):
        return self._tts.getMaxSpeechInputLength()
    def get_voice(self):
        return self._tts.getVoice()
    def get_voices(self):
        a=self._tts.getVoices()
        if a:
            return a.toArray()

    ####bools
    def is_language_available(self,loc):
        return self._tts.isLanguageAvailable(loc)
    def is_speaking(self):
        return self._tts.isSpeaking()





