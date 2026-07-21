import numpy as np
import config as cfg 
import math

class Wavetable():
    def get_wave(self, frame: float):
        return math.sin(frame)

class SineWave(Wavetable):
    def get_wave(self, frame: float):
        return math.sin(frame * np.pi * 2)

class SquareWave(Wavetable):
    def get_wave(self, frame: float):
        if abs(math.sin(frame) / np.pi) != 0:
            return (math.sin(frame) / np.pi) / (abs(math.sin(frame) / np.pi))
        else:
            return 0

class SawWave(Wavetable):
    def get_wave(self, frame: float):
        return frame - round(frame)
