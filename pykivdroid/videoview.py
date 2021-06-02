
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty
from kivy.utils import platform
from pykivdroid import mActivity,VideoView,LinearLayout,ViewGroupNLayoutParams,MediaController,Gravity,run_on_ui_thread



class AndroidVideoView(Widget):
    videoview=None
    controller=BooleanProperty(True)
    def __init__(self,uri=None,**k):
        super().__init__(**k)


        

        self._init()
        
        
       
    
    @run_on_ui_thread        
    def _init(self,):
        #print("aaaaaaaaaa")
        if platform=="android":
            #print("aa")
            #mActivity = PythonActivity.mActivity 
            self.videoview=VideoView(mActivity)
            self.videoview.setMediaController(MediaController(mActivity))
            #self.videoview.setVideoURI(uri)
            self.layout = LinearLayout(mActivity)
            self.layout.setOrientation(LinearLayout.VERTICAL)
            self.layout.setGravity(Gravity.CENTER)
            self.layout.addView(self.videoview, self.width, self.height)
            mActivity.addContentView(self.layout, ViewGroupNLayoutParams(-1,-1))
            #self.videoview.start()

    @run_on_ui_thread
    def on_size(self, instance, size):
        if self.videoview:
        
            params = self.layout.getLayoutParams()
            params.width = self.width
            params.height = self.height
            self.layout.setLayoutParams(params)
            param = self.videoview.getLayoutParams()
            param.width = self.width
            param.height = self.height
            self.videoview.setLayoutParams(param)


    @run_on_ui_thread
    def start(self,):
        if self.videoview:
            self.videoview.setZOrderMediaOverlay(True);

            self.videoview.setZOrderOnTop(True)
            self.videoview.start()

    @run_on_ui_thread
    def pause(self,):
        if self.videoview:
            self.videoview.pause()

    @run_on_ui_thread
    def resume(self,):
        if self.videoview:
            self.videoview.resume()
    @run_on_ui_thread
    def stop_playback(self,):
        if self.videoview:
            self.videoview.stopPlayback()
    @run_on_ui_thread
    def suspend(self,):
        if self.videoview:
            self.videoview.suspend()
    
    @run_on_ui_thread
    def seek_to(self,ms):
        if self.videoview:
            self.videoview.seekTo(ms)





    @run_on_ui_thread
    def set_video_uri(self,uri):
        if self.videoview:
            self.videoview.setVideoURI(uri)
    @run_on_ui_thread
    def set_video_path(self,path):
        if self.videoview:
            self.videoview.setVideoPath(path)
    






     ########bools        
    @run_on_ui_thread
    def is_playing(self,):
        if self.videoview:
            return self.videoview.isPlaying()
    @run_on_ui_thread
    def get_duration(self,):
        if self.videoview:
            return self.videoview.getDuration()
    @run_on_ui_thread
    def get_current_position(self,):
        if self.videoview:
            return self.videoview.getCurrentPosition()
    @run_on_ui_thread
    def get_audio_session_id(self,):
        if self.videoview:
            return self.videoview.getAudioSessionId()



    @run_on_ui_thread
    def can_pause(self,):
        if self.videoview:
            return self.videoview.canPause()
    @run_on_ui_thread
    def can_seek_backward(self,):
        if self.videoview:
            return self.videoview.canSeekBackward()
    @run_on_ui_thread
    def can_seek_forward(self,):
        if self.videoview:
            return self.videoview.canSeekForward()
    @run_on_ui_thread
    def can_pause(self,):
        if self.videoview:
            return self.videoview.canPause()










 
