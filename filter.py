import matplotlib.pyplot as plt
import numpy as np
import wave

fig = plt.figure(figsize=(6, 10))
axisA = plt.subplot(311)
axisB = plt.subplot(312)
axisC = plt.subplot(313)

def click_figure(event):
    if event.button == 1 and event.inaxes in [fig.axes[2]]:
        print(event)

if __name__ == "__main__":
    wav = wave.open("guitar sample.wav", "rb")
    fs = wav.getframerate()
    dt = 1.0 / fs
    num = wav.getnframes()
    times = float(num) / float(fs)
    
    X = np.arange(0, times, dt)
    Y = np.frombuffer(wav.readframes(num), dtype="int16").astype("float32")
    G = np.gradient(Y, dt)

    axisA.plot(X, Y)
    axisA.set_title("The time history of the waveform")
    axisB.plot(X, np.abs(G))
    axisB.set_title("The time history of the differentiation")
    axisC.hist(np.abs(G), bins=1000, log=True)
    axisC.set_title("Differentiate waveforms\nLC=Add, RC=Reset, MC=Generate")

    plt.tight_layout()

    fig.canvas.mpl_connect("button_press_event", click_figure)
    plt.show()