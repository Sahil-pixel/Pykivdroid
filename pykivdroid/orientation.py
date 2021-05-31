from pykivdroid import mActivity,orientation_dict,Logger

def get_orientation():
    return mActivity.getResources().getConfiguration().orientation

def set_orientation(mode='all'):
        try:
            if mode in orientation_dict:
                mActivity.setRequestedOrientation(orientation_dict[mode])
        except Exception as e:
            Logger.error("Pykivdroid: "+str(e))

