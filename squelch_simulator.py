import numpy as np

def generate_wave(freq, amp, duration=1.0, samples=1000):
    t = np.linspace(0, duration, samples)
    wave = amp * np.sin(2 * np.pi * freq * t)
    return t, wave