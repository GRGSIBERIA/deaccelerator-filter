import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

pastdata = [0.0]
fs = 0
dt = 0
lines = None
x = None

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    
    postdata = np.gradient(indata, dt)
    print(postdata)
    outdata[:] = postdata
    lines.set_data(x, outdata)

    pastdata[-1:] = indata
    outdata[:] = postdata[1:]
    plt.pause(1)


if __name__ == "__main__":
    fs = 44100
    sd.default.samplerate = fs
    print(sd.query_devices())
    dt = 1.0 / float(fs)
    sd.default.channels = 2
    sd.default.dtype = "float32"
    sd.default.blocksize = 512
    print(sd.default.blocksize)
    y = np.zeros(sd.default.blocksize)
    x = np.arange(0, sd.default.blocksize, 1)

    plt.figure(figsize=(6, 4))
    lines, = plt.plot(x, y)

    with sd.Stream(channels=2, callback=callback):
        sd.sleep(int(60 * 60 * 1000))