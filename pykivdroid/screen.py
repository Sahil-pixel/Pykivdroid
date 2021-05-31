from pykivdroid import mActivity,WindowManagerNLayoutParams,Window,run_on_ui_thread,View

@run_on_ui_thread
def set_full_screen():
    return mActivity.getWindow().getDecorView().setSystemUiVisibility( 
                   View.SYSTEM_UI_FLAG_FULLSCREEN 
                   |View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN 
                   | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY  
                   | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                   | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION)
    

