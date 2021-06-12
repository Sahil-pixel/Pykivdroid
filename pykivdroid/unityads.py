
'''
Programmer SK SAHIL 
https://github.com/Sahil-pixel

1)Download Unity-ads.aar from unity ads 

2)Add Unity-ads.aar to your /libs folder

update buildozer.spec 

android.add_aars = ./libs/*.aar
android permissions = INTERNET,ACCESS_NETWORK_STATE
3) Add the following acitivites to your Android manifest file before the end of </application> tag.
you can find Android manifest file.
your_project_folder/.buildozer/android/platform/build-armeabi-v7a/dists/test_project__armeabi-v7a/templates/AndroidManifest.tmpl.xml
 
 <activity
     android:name="com.unity3d.services.ads.adunit.AdUnitActivity"
     android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
     android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
     android:hardwareAccelerated="true" />

  <activity
     android:name="com.unity3d.services.ads.adunit.AdUnitTransparentActivity"
     android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
     android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen"
     android:hardwareAccelerated="true" />

  <activity
     android:name="com.unity3d.services.ads.adunit.AdUnitTransparentSoftwareActivity"
     android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
     android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen"
     android:hardwareAccelerated="false" />

  <activity
     android:name="com.unity3d.services.ads.adunit.AdUnitSoftwareActivity"
     android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
     android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
     android:hardwareAccelerated="false" />




'''

from pykivdroid import PythonJavaClass,LinearLayout,ViewGroupNLayoutParams,Gravity,java_method,cast,run_on_ui_thread,mActivity,autoclass
import logging

#UnityAdsListener = autoclass("com.unity3d.ads.IUnityAdsListener")
UnityAds = autoclass("com.unity3d.ads.UnityAds")
UnityAdsNFinishState=autoclass('com.unity3d.ads.UnityAds$FinishState')

BannerView=autoclass("com.unity3d.services.banners.BannerView")
UnityBannerSize=autoclass("com.unity3d.services.banners.UnityBannerSize")
logging.info("Pykivdroid : unityads : Modules imported \n")


class UnityHandler():
   _mode="interstitial"
   _test_mode=True
   _ads_id=''
   _app_id=''

   callback=None
   def __init__(self,app_id='',):
      #self.callback=callback
      self._app_id=app_id
      self._banner=None

   def init_ads(self,test_mode=True,ads_type="interstitial",callback=None):
      if ads_type=="interstitial" or "reward":
         self.callback=callback
         self._mode=ads_type
         self._test_mode=test_mode
         self.new_ad_listener = UnityAdsListener(self._mode,self.callback)
         UnityAds.setListener(self.new_ad_listener)
         UnityAds.initialize(mActivity,self._app_id,self._test_mode)
   



         
      else:
         logging.info("Pykivdroid : unityads : "+str(ads_type)+" invalid ads_type")
   

   def show_ads(self,ads_id):
      if UnityAds.isReady(ads_id):
         try:
            UnityAds.show(mActivity, ads_id)
         except Exception as e:
            print(e)
      else:
         logging.info("Unity ads not ready and thus has not been loaded")


   @run_on_ui_thread 
   def init_banner_ads(self,ads_id,test_mode=True,top_pos=True):

      UnityAds.initialize(mActivity,self._app_id,None,test_mode,True)
      self.banner_listener=UnityBannerListener()

      self._banner=BannerView(mActivity,ads_id,UnityBannerSize(320,50))
      
      self._banner.setListener(self.banner_listener)
      #adLayoutParams = ViewGroupNLayoutParams(ViewGroupNLayoutParams.MATCH_PARENT, ViewGroupNLayoutParams.WRAP_CONTENT)
      #self._banner.setLayoutParams(adLayoutParams)

      self._layout = LinearLayout(mActivity)
      
      self._layoutParams = ViewGroupNLayoutParams(ViewGroupNLayoutParams.MATCH_PARENT, ViewGroupNLayoutParams.MATCH_PARENT)
      self._layout.setLayoutParams(self._layoutParams)
      if not top_pos:
         self._layout.setGravity(Gravity.BOTTOM | Gravity.CENTER)
         #print("#########")
      if top_pos:
         #print("top pos")
         self._layout.setGravity(Gravity.TOP | Gravity.CENTER)

      

      mActivity.addContentView(self._layout, self._layoutParams)

   def load_banner(self,):
      if self._banner:
         self._banner.load()

   @run_on_ui_thread
   def show_banner(self):
      if self._banner:
         self._layout.removeView(self._banner)
         self._layout.addView(self._banner)
   @run_on_ui_thread
   def hide_banner(self):
      if self._banner:
         #self._banner.removeAllViews()
         self._layout.removeView(self._banner)
         #self._banner=None


     













class UnityAdsListener(PythonJavaClass):
   __javainterfaces__= ['com/unity3d/ads/IUnityAdsListener']
   __javacontext__= 'app'
   _ads_mode="interstitial"
   _callback=None

   def __init__(self,ads_type,callback):
      self._ads_type=ads_type
      self._callback=callback
   


   @java_method('(Ljava/lang/String;)V')
   def onUnityAdsReady(self,inter_id):
      logging.info("Pykivdroid : unityads : ADS are ready! "+ str(inter_id) + " \n")
   
   @java_method('(Ljava/lang/String;)V')
   def onUnityAdsStart(self,inter_id):
      logging.info("Pykivdroid: unityads : ADS are starting! " + str(inter_id) + "\n")
   

   @java_method('(Ljava/lang/String;Lcom/unity3d/ads/UnityAds$FinishState;)V')
   def onUnityAdsFinish(self,inter_id,finish_state):
      logging.info("Pykivdroid : unityads : ADS are FINISHED! "+str(finish_state) + " \n")
      if self._ads_type=="reward":

         if finish_state.equals(UnityAdsNFinishState.COMPLETED):
            reward_viewed=True
            logging.info("Pykivdroid: unityads :Unity Reward AD shown and Rewarded Succesfully\n")

         elif finish_state.equals(UnityAdsNFinishState.SKIPPED):
            reward_viewed=False
         if self._callback:
            self._callback(reward_viewed)
         else:
            logging.info("Pykivdroid: unityads :callback is None")

   @java_method('(Lcom/unity3d/ads/UnityAds$UnityAdsError;Ljava/lang/String;)V')
   def onUnityAdsError(self,error, message):
      logging.info("Pykivdroid: unityads : ADS are in error!\n")







class  UnityBannerListener(PythonJavaClass):

   __javainterfaces__= ['com/unity3d/services/banners/BannerView$IListener']
   __javacontext__= 'app'

   @java_method('(Lcom/unity3d/services/banners/BannerView;)V')
   def onBannerLoaded(self,bannerAdView):
      logging.info("Pykivdroid : unityads : Banner ADS are in loaded!")


   @java_method('(Lcom/unity3d/services/banners/BannerView;Lcom/unity3d/services/banners/BannerErrorInfo;)V')
   def onBannerFailedToLoad(self,bannerAdView, errorInfo):
      logging.info("Pykivdroid : unityads : Banner ADS are loading faild! "+str(errorInfo.errorMessage))

   @java_method('(Lcom/unity3d/services/banners/BannerView;)V')
   def onBannerClick(self,bannerAdView):
      logging.info('Pykivdroid : unityads :  Banner clicked')

   @java_method('(Lcom/unity3d/services/banners/BannerView;)V')
   def onBannerLeftApplication(self,bannerAdView):
      logging.info("Pykivdroid : UnityAds : Banner left application!")

