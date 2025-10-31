from scipy.fftpack import fft
import numpy as np

payload_map = {
    'Delight': (1200, 'red'),
    'Embarrassment': (300, 'yellow'),
    'Disruption': (600, 'green'),
    'Nostalgia': (900, 'blue')
}

def analyze_fft(wave, t):
    fft_vals = fft(wave)
    fft_freqs = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
    return fft_freqs[:500], np.abs(fft_vals[:500])