import sounddevice
from scipy.io.wavfile import write # io means input/output and wavefile is used to export recording into wavefile

def rahul_voice_recorder(seconds,file):
    print("Recording started...")
    rahul_recording=sounddevice.rec((seconds*44100),samplerate=44100,channels=2)
    sounddevice.wait()
    write(file,44100,rahul_recording)
    print("Recording is Finished")

rahul_voice_recorder(10,"recordsave.wav")
