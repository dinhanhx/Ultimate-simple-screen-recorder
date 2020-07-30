from setting import load_settings

def make_mic(cps, stop_key):
    pass

def make_speaker(cps, stop_key):
    pass

def make_audio():
    setting = load_settings()
    if setting["mic"]:
        make_mic(setting["fs"], setting["stop key"])

    if setting["speaker"]:
        make_speaker(setting["fs"], setting["stop key"])
