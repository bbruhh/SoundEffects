import scipy.io.wavfile
import numpy as np
import effect


def read_wav(path):
    return scipy.io.wavfile.read(path)


def write_wav(path, data, sample_rate):
    data = data.astype(np.int16) #type int16 signed wav file
    scipy.io.wavfile.write(path, sample_rate, data)


rate, wav = read_wav("KZ2.wav")
echo = effect.Echo(rate, 0.99, 0.40, 5, True)
write_wav("echoed.wav", echo.apply(wav), rate)

rate, wav = read_wav("KZ2.wav")
echo = effect.Echo(rate, delay=0.80, decay=0.40, repeats=2, prolong=True)
noise = effect.Noise(mu=0, sigma=25, effect=echo)
write_wav("echo_then_noise.wav", noise.apply(wav), rate)

rate, wav = read_wav("KZ2.wav")
noise = effect.Noise(mu=0, sigma=25)
echo = effect.Echo(rate, delay=0.80, decay=0.40, repeats=2, prolong=True, effect=noise)
write_wav("noise_then_echo.wav", echo.apply(wav), rate)