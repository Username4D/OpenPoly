import pygame
import osc
import wavetables
from pygame.constants import KEYDOWN
import sounddevice as sd

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.update()

run = True
note_keybinds = {97: 1, 119: 2, 115: 3, 101: 4, 100: 5, 102: 6, 116: 7, 103: 8, 121: 9, 104: 10, 117: 11, 106: 12}

osc_1 = osc.Osc(wavetables.SawWave())



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key in note_keybinds:
                osc_1.pitches.append(note_keybinds[event.key] + 24)
        if event.type == pygame.KEYUP:
            if event.key in note_keybinds:
                osc_1.pitches.remove(note_keybinds[event.key] + 24)
    sd.play(osc_1.render_buffer(10000))
    sd.wait()
