import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chemms.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chemms2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cheemsmamado.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cheemsmamado2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cheembat.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/cheembat2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/dogjump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/jumpingdog.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/cheembat.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitob.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitob2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitoescudo.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitoescudo2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitobate.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitobate2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zop.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zop2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zop3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/creeper.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/creeper2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/creeper3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
HOPE = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/hope.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/apple.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/bat.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG2 = [
     pygame.image.load(os.path.join(IMG_DIR, 'Other/back/dos2.jpg')),
     pygame.image.load(os.path.join(IMG_DIR, 'Other/back/tres2.jpg')),

]
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitob.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/chikitob2.png")),
]

HAMMER_POWER_UP = 10
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
HEART_COUNT = 7

pygame.mixer.init()
SOUNDS = [
    pygame.mixer.Sound("dino_runner/assets/Dino/sounds/Jump.wav"),
    pygame.mixer.Sound("dino_runner/assets/Dino/sounds/Grow.wav"),
    pygame.mixer.Sound("dino_runner/assets/Dino/sounds/Die.wav"),
    pygame.mixer.Sound("dino_runner/assets/Dino/sounds/Dark_Die.wav"),
    pygame.mixer.Sound("dino_runner/assets/Dino/sounds/bonk.wav"),

]

