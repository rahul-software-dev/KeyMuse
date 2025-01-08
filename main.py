import sounddevice as sd
import numpy as np
import tkinter as tk
from ui_design import KeyMuseUI

# Define frequency for each note (in Hz) for a basic scale
NOTE_FREQUENCIES = {
    'a': 261.63,  # C4
    's': 293.66,  # D4
    'd': 329.63,  # E4
    'f': 349.23,  # F4
    'g': 392.00,  # G4
    'h': 440.00,  # A4
    'j': 493.88,  # B4
    'k': 523.25,  # C5
}

# Sound synthesis parameters
SAMPLE_RATE = 44100  # Samples per second
DURATION = 0.3       # Duration of each note in seconds

def generate_waveform(frequency, waveform_type="sine"):
    """Generates waveform samples for a given frequency and waveform type."""
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), False)
    
    if waveform_type == "sine":
        waveform = 0.5 * np.sin(2 * np.pi * frequency * t)
    elif waveform_type == "square":
        waveform = 0.5 * np.sign(np.sin(2 * np.pi * frequency * t))
    elif waveform_type == "sawtooth":
        waveform = 0.5 * (2 * (t * frequency - np.floor(0.5 + t * frequency)))
    elif waveform_type == "noise":
        waveform = 0.5 * np.random.uniform(-1, 1, t.shape)
    else:
        raise ValueError("Unknown waveform type")
    
    return waveform.astype(np.float32)

class KeyMuseApp:
    def __init__(self, root):
        self.root = root
        self.waveform_type = "sine"  # Default waveform
        self.ui = KeyMuseUI(root, self.set_waveform)
        self.root.bind("<KeyPress>", self.key_press)

    def set_waveform(self, waveform_type):
        """Sets the waveform type (sine, square, sawtooth, noise)."""
        self.waveform_type = waveform_type

    def key_press(self, event):
        """Handles key press events and plays the corresponding sound."""
        key = event.char
        frequency = NOTE_FREQUENCIES.get(key)
        if frequency:
            waveform = generate_waveform(frequency, self.waveform_type)
            sd.play(waveform, samplerate=SAMPLE_RATE)

def main():
    root = tk.Tk()
    app = KeyMuseApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
