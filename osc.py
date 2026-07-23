import numpy as np
import wavetables
import config as cfg
import sounddevice as sd

class Osc():
    wavetable: wavetables.Wavetable
    volume: float = 1
    pitch_offset: int = 0
    fine_offset: float = 0
    pitch: int = -1
    offset: int = 0
    
    def __init__(self, _wavetable: wavetables.Wavetable):
        self.wavetable = _wavetable
    
    def render_buffer(self, buffer_length: int):
        if self.pitch != -1:
            duration: float = buffer_length / cfg.sample_rate
            frequency = 2.0 ** ((float(self.pitch - 49 + self.pitch_offset)) / 12.0) * 440.0
            wave_snapshot_length: int = round(cfg.sample_rate / frequency)
            wave_snapshot = np.array([])
            for i in range(0, wave_snapshot_length):
                wave_snapshot = np.append(wave_snapshot, self.wavetable.get_wave(float(i) / float(wave_snapshot_length)))
            generated_wave = np.array([])
            self.offset += buffer_length % wave_snapshot_length
            self.offset = self.offset % wave_snapshot_length
            generated_wave = np.concatenate([generated_wave, wave_snapshot])
            generated_wave = np.delete(generated_wave, np.s_[0:self.offset])
            while len(generated_wave) < buffer_length:
                generated_wave = np.concatenate([generated_wave, wave_snapshot])

            generated_wave = np.resize(generated_wave, buffer_length)
            
            return generated_wave
        else:
            array = np.array([])
            array.resize(buffer_length)
            return array
