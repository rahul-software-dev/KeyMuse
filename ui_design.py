from sounds import SoundPlayer

class KeyMuseUI:
    def __init__(self):
        self.player = SoundPlayer()

    def select_instrument(self):
        print("Available instruments: sine, square, sawtooth, noise")
        choice = input("Select instrument: ").strip().lower()
        self.player.set_instrument(choice)

    def play_notes(self):
        print("Press keys to play notes (a, s, d, f, g, h, j, k) or 'q' to quit.")
        while True:
            key = input("Key: ").strip().lower()
            if key == 'q':
                break
            self.player.play_sound(key)
print('hi')