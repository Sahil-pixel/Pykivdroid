from kivy.utils import platform
from kivy.logger import Logger
import webbrowser
if platform == "android":
    try:
        #from kivy.core.window import Window
        from jnius import autoclass, cast, JavaException,PythonJavaClass,java_method
        from android.runnable import run_on_ui_thread
        from android.permissions import request_permissions, Permission
        from android import activity
        #A
        AndroidActivity = autoclass('android.app.Activity')
        ActivityInfo = autoclass('android.content.pm.ActivityInfo')
        AudioManager = autoclass('android.media.AudioManager')
        ArrayList = autoclass('java.util.ArrayList')
        
        #B
        BatteryManager = autoclass("android.os.BatteryManager")
        BitmapFactory = autoclass('android.graphics.BitmapFactory')
        Build = autoclass("android.os.Build")
        Bundle = autoclass('android.os.Bundle')

        #C

        Camera = autoclass('android.hardware.Camera')
        

        Color = autoclass("android.graphics.Color")
        Context = autoclass('android.content.Context')
        ConnectivityManager = autoclass('android.net.ConnectivityManager')
        Configuration = autoclass("android.content.res.Configuration")
        #D
        DisplayMetrics = autoclass('android.util.DisplayMetrics')
        
        #E
        Environment = autoclass("android.os.Environment")
        #F
        File = autoclass('java.io.File')
        #G
        Gravity=autoclass('android.view.Gravity')
        #I
        Intent = autoclass('android.content.Intent')
        IntentFilter = autoclass("android.content.IntentFilter")
        #J
        #K
        KeyEvent = autoclass('android.view.KeyEvent')

        #L
        Locale = autoclass('java.util.Locale')
        LinearLayout = autoclass('android.widget.LinearLayout')
        
        #M
        MediaController=autoclass('android.widget.MediaController')
        MediaPlayer = autoclass('android.media.MediaPlayer')
        MediaRecorder = autoclass('android.media.MediaRecorder')
        
        #N
        #O
        
        #P
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        PackageManager = autoclass('android.content.pm.PackageManager')
        Point = autoclass("android.graphics.Point")

        #R
        Rect = autoclass('android.graphics.Rect')()
        RecognizerIntent = autoclass('android.speech.RecognizerIntent')
        RecognitionListener = autoclass('android.speech.RecognitionListener')
        
        Runtime = autoclass('java.lang.Runtime')

        #S
        Settings = autoclass('android.provider.Settings')
        SpeechRecognizer = autoclass('android.speech.SpeechRecognizer')
        String = autoclass("java.lang.String")
        StrictMode = autoclass('android.os.StrictMode')
        StatFs = autoclass("android.os.StatFs")
        SurfaceTexture = autoclass("android.graphics.SurfaceTexture")
        
        #T
        TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
        Toast = autoclass('android.widget.Toast')
        #U
        Uri = autoclass('android.net.Uri')
        URLConnection = autoclass("java.net.URLConnection")
        #V
        
        
        View = autoclass('android.view.View')
        ViewGroup = autoclass('android.view.ViewGroup')
        VideoView=autoclass('android.widget.VideoView')
        #W
        
        WallpaperManager = autoclass('android.app.WallpaperManager')
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        Window=autoclass('android.view.Window')
        



        ######Nested classes 
        # N used to indicate nested class
        #A
        ActivityManagerNMemoryInfo = autoclass('android.app.ActivityManager$MemoryInfo')
        
        #B
        BuildNVERSION = autoclass('android.os.Build$VERSION')
        BuildNVERSION_CODES = autoclass("android.os.Build$VERSION_CODES")
        #C
        CameraNCameraInfo=autoclass('android.hardware.Camera$CameraInfo')
        CameraNParameters = autoclass("android.hardware.Camera$Parameters")
        #D
        DownloadNManagerRequest = autoclass("android.app.DownloadManager$Request")
        #E
        #F
        #G
        #H
        #I
        #J
        #K
        #L
        #M
        MediaRecorderNAudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')
        MediaRecorderNAudioSource = autoclass('android.media.MediaRecorder$AudioSource')
        MediaRecorderNOutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
        #N
        #O
        #P
        #Q
        #R
        #S
        SettingsNSystem = autoclass('android.provider.Settings$System')
        #T
        #U
        #V
        ViewGroupNLayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
        
        #W
        WindowManagerNLayoutParams= autoclass('android.view.WindowManager$LayoutParams')
        #X
        #Y
        #Z






        #app's activity
        mActivity = PythonActivity.mActivity
        
        
        
        
        
        
        
        
        
        
       
        
        
        
        


        packages = {
            "whatsapp": "com.whatsapp",
            "facebook": "com.facebook.katana",
            "facebookLite": "com.facebook.lite",
            "oldFacebook": "com.facebook.android",
            "linkedin": "com.linkedin.android",
            "fbMessenger": "com.facebook.orca",
            "fbMessengerLite": "com.facebook.mlite",
            "tiktok": "com.zhiliaoapp.musically",
            "tiktokLite": "com.zhiliaoapp.musically.go",
            "twitter": "com.twitter.android",
            "twitterLite": "com.twitter.android.lite",
            "telegram": "org.telegram.messenger",
            "telegramX": "org.thunderdog.challegram",
            "snapchat": "com.snapchat.android"
        }

    except BaseException:
        Logger.error(
            "Pyandroid: Cannot load classes by Pyjnius. Make sure requirements installed"
        )


    ###########dict of orientation
    orientation_dict={
    'portrait':ActivityInfo.SCREEN_ORIENTATION_PORTRAIT,
    'landscape':ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE,
    'behind':ActivityInfo.SCREEN_ORIENTATION_BEHIND,
    'full_sensor':ActivityInfo.SCREEN_ORIENTATION_FULL_SENSOR,
    'full_user':ActivityInfo.SCREEN_ORIENTATION_FULL_USER,
    'locked':ActivityInfo.SCREEN_ORIENTATION_LOCKED,
    'no_sensor':ActivityInfo.SCREEN_ORIENTATION_NOSENSOR,
    'user': ActivityInfo.SCREEN_ORIENTATION_USER,
    'user_portrait': ActivityInfo.SCREEN_ORIENTATION_USER_PORTRAIT,
    'user_landscape': ActivityInfo.SCREEN_ORIENTATION_USER_LANDSCAPE,
    'unspecified': ActivityInfo.SCREEN_ORIENTATION_UNSPECIFIED,
    'sensor_portrait':ActivityInfo.SCREEN_ORIENTATION_SENSOR_PORTRAIT,
    'sensor_landscape':ActivityInfo.SCREEN_ORIENTATION_SENSOR_LANDSCAPE,
    'sensor':ActivityInfo.SCREEN_ORIENTATION_SENSOR,
    'reverse_portrait':ActivityInfo.SCREEN_ORIENTATION_REVERSE_PORTRAIT,
    'reverse_landscape':ActivityInfo.SCREEN_ORIENTATION_REVERSE_LANDSCAPE,
    }

    def text_to_speech(text, lang=Locale.US):
            tts = TextToSpeech(mActivity, None)
            tts.setLanguage(lang)
            tts.speak(str(text), TextToSpeech.QUEUE_FLUSH, None)

    def launch_app(app_package, app_activity):
        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)
        intent.setClassName(app_package, app_activity)
        return mActivity.startActivity(intent)

    def toast(message):
        return PythonActivity.toastError(str(message))


    def download_manager(title, description, url, folder, file_name):
        uri = Uri.parse(str(url))
        dm = cast("android.app.DownloadManager", mActivity.getSystemService(Context.DOWNLOAD_SERVICE))
        request = DownloadManagerNRequest(uri)
        request.setTitle(str(title))
        request.setDescription(str(description))
        ########notification bar
        request.setNotificationVisibility(DownloadManagerNRequest.VISIBILITY_VISIBLE)
        request.setDestinationInExternalPublicDir(folder, str(file_name))
        dm.enqueue(request)

    
    @run_on_ui_thread
    def write_settings(sdk_int,version_code):
        if sdk_int>=version_code:

            if SettingsNSystem.canWrite(mActivity.getApplicationContext()):
                print("can write")
            else:
                intent=Intent(Settings.ACTION_MANAGE_WRITE_SETTINGS)
                intent.setData(Uri.parse("package:" + mActivity.getPackageName()))
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                mActivity.startActivity(intent)





    def share_file(path, title='Share', chooser=True, app_package=None, call_playstore=True, error_msg=""):
        path = str(path)
        StrictMode.disableDeathOnFileUriExposure()
        shareIntent = Intent(Intent.ACTION_SEND)
        shareIntent.setType("*/*")
        imageFile = File(path)
        uri = Uri.fromFile(imageFile)
        parcelable = cast('android.os.Parcelable', uri)
        shareIntent.putExtra(Intent.EXTRA_STREAM, parcelable)

        if app_package:
            app_package = packages[app_package] if app_package in packages else None
            try:
                shareIntent.setPackage(String(app_package))
            except JavaException:
                if call_playstore:
                    webbrowser.open(f"http://play.google.com/store/apps/details?id={app_package}")
                toast(error_msg) if error_msg else Logger.error("Pyandroid: Specified Application is unavailable")
                return

        if chooser:
            chooser = Intent.createChooser(shareIntent, String(title))
            mActivity.startActivity(chooser)
        else:
            mActivity.startActivity(shareIntent)



 
