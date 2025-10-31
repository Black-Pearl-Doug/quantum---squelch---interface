import tkinter as tk
from tkinter import ttk
from squelch_simulator import generate_wave
from fft_analyzer import analyze_fft
import matplotlib.pyplot as plt

def launch_gui():
    root = tk.Tk()
    root.title("Quantum Squelch Interface")

    # Frequency input
    ttk.Label(root, text="Frequency (Hz):").grid(column=0, row=0)
    freq_entry = ttk.Entry(root)
    freq_entry.grid(column=1, row=0)
    freq_entry.insert(0, "300")

    # Amplitude input
    ttk.Label(root, text="Amplitude:").grid(column=0, row=1)
    amp_entry = ttk.Entry(root)
    amp_entry.grid(column=1, row=1)
    amp_entry.insert(0, "1.0")

    # Temperature slider
    ttk.Label(root, text="Membrane Temperature:").grid(column=0, row=2)
    temp_slider = ttk.Scale(root, from_=0, to=100, orient='horizontal')
    temp_slider.grid(column=1, row=2)

    # Emotional payload selector
    ttk.Label(root, text="Emotional Payload:").grid(column=0, row=3)
    emotion_combo = ttk.Combobox(root, values=["Delight", "Embarrassment", "Disruption", "Nostalgia"])
    emotion_combo.grid(column=1, row=3)
    emotion_combo.current(0)

    # Archive log
    archive_log = tk.Text(root, height=6, width=50)
    archive_log.grid(column=0, row=4, columnspan=2)
    archive_log.insert(tk.END, "Mnemonic Archive Initialized...\n")

    # Run simulation
    def run_simulation():
        freq = float(freq_entry.get())
        amp = float(amp_entry.get())
        emotion = emotion_combo.get()
        temp = temp_slider.get()
        t, wave = generate_wave(freq, amp)
        freqs, fft_vals = analyze_fft(wave, t)

        plt.figure(figsize=(8, 4))
        plt.plot(freqs, fft_vals, label=emotion)
        plt.title("FFT Squelch Harmonics")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.legend()
        plt.show()

        archive_log.insert(tk.END, f"Squelch logged: {emotion} @ {freq}Hz, Temp={temp}°\n")

    ttk.Button(root, text="Run Squelch Simulation", command=run_simulation).grid(column=0, row=5, columnspan=2)

    root.mainloop()