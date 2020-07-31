import sounddevice as sd
from scipy.io.wavfile import write
from numpy import vstack

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

merec_list = []
merec_temp = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
merec_list.append(merec_temp)
merec_temp = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
merec_list.append(merec_temp)

merec = vstack(merec_list)

write('output.wav', fs, merec)  # Save as WAV file
