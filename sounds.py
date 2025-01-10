# sounds.py

import numpy as np
import pygame

class SoundPlayer:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
        self.sample_rate = 44100  # Sample rate for sound generation
        self.note_frequencies = {
            pygame.K_a: 261.63,  # C4
            pygame.K_s: 293.66,  # D4
            pygame.K_d: 329.63,  # E4
            pygame.K_f: 349.23,  # F4
            pygame.K_g: 392.00,  # G4
            pygame.K_h: 440.00,  # A4
            pygame.K_j: 493.88,  # B4
            pygame.K_k: 523.25   # C5
        }
        self.current_waveform = 'sine'  # Default waveform

    def set_waveform(self, waveform):
        # Ensure only valid waveforms are set
        if waveform in ['sine', 'square', 'sawtooth']:
            self.current_waveform = waveform
        else:
            print("Invalid waveform. Defaulting to 'sine'.")
            self.current_waveform = 'sine'

    def generate_sound(self, frequency, duration=0.5):
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        if self.current_waveform == 'sine':
            sound_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
        elif self.current_waveform == 'square':
            sound_wave = 0.5 * np.sign(np.sin(2 * np.pi * frequency * t))
        elif self.current_waveform == 'sawtooth':
            sound_wave = 0.5 * (2 * (t * frequency - np.floor(0.5 + t * frequency)))

        sound_wave = (sound_wave * 32767).astype(np.int16)  # Convert to 16-bit PCM
        return pygame.sndarray.make_sound(sound_wave)

    def play_sound(self, key):
        if key in self.note_frequencies:
            frequency = self.note_frequencies[key]
            sound = self.generate_sound(frequency)
            sound.play()
        else:
            print(f"No sound mapped for key: {key}")
