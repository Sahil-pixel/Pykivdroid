from pykivdroid import SettingsNSystem,mActivity

'''
Date 28/May/2021

Required Permissions:
    WRITE_SETTINGS
'''
def get_brightness():
    SettingsNSystem.putInt(mActivity.getContentResolver(),
        SettingsNSystem.SCREEN_BRIGHTNESS_MODE,
        SettingsNSystem.SCREEN_BRIGHTNESS_MODE_MANUAL)
    cr_level = SettingsNSystem.getInt(mActivity.getContentResolver(),SettingsNSystem.SCREEN_BRIGHTNESS)
    return (cr_level / 255.) * 100

def set_brightness(level):
        SettingsNSystem.putInt(mActivity.getContentResolver(),SettingsNSystem.SCREEN_BRIGHTNESS,(level / 100.) * 255)




