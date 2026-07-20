import numpy as np
import wavetables
import config as cfg
import sounddevice as sd

class Osc():
    wavetable: wavetables.Wavetable
    volume: float = 1
    pitch_offset: int = 0
    fine_offset: float = 0
    pitches: list = []

    def __init__(self, _wavetable: wavetables.Wavetable):
        self.wavetable = _wavetable
    
    def render_buffer(self, buffer_length: int):
        duration: float = buffer_length / cfg.sample_rate
        output = np.array([])
        output = np.resize(output, buffer_length)
        for i in self.pitches:
            frequency = 2.0 ** ((float(i - 49 + self.pitch_offset)) / 12.0) * 440.0
            wave_snapshot_length: int = round(cfg.sample_rate / frequency)
            wave_snapshot = np.array([])
            for i in range(0, wave_snapshot_length):
                wave_snapshot = np.append(wave_snapshot, self.wavetable.get_wave(float(i) / float(wave_snapshot_length)))
            generated_wave = np.array([])

            while len(generated_wave) < buffer_length:
                generated_wave = np.concatenate([generated_wave, wave_snapshot])
            print(generated_wave)

            generated_wave = np.resize(generated_wave, buffer_length)
            output = np.add(output, generated_wave)
        return output
default_osc: Osc = Osc(wavetables.SineWave())
default_osc.pitches = [48]
sd.play(default_osc.render_buffer(44100))
sd.wait()