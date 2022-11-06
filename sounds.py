import pygame
import time

pygame.mixer.init()

def correctAnswerSound():
    pygame.mixer.music.set_volume(1)    
    pygame.mixer.music.load("./assets/sounds/correctAnswer.wav")
    pygame.mixer.music.play(loops=0)
def wrongAnswerSound():
    pygame.mixer.music.set_volume(1)    
    pygame.mixer.music.load("./assets/sounds/wrongAnswer.mp3")
    pygame.mixer.music.play(loops=0)

def gameStartSound():
    pygame.mixer.music.set_volume(1)    
    pygame.mixer.music.load("./assets/sounds/gameStart.mp3")
    pygame.mixer.music.play(loops=0)

def comboSound():
    pygame.mixer.music.set_volume(1)    
    pygame.mixer.music.load("./assets/sounds/combo.mp3")
    pygame.mixer.music.play(loops=0)

def mainMenuSound():
    pygame.mixer.music.set_volume(1)    
    pygame.mixer.music.load("./assets/sounds/mainMenu.mp3")
    pygame.mixer.music.play(loops=10)
    pygame.mixer.music.set_volume(1)

def winGameSound():
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.load("./assets/sounds/winGame.mp3")
    pygame.mixer.music.play(loops=0)
