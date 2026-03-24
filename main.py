
# import pygame, sys
# import os
# import random

# # 🔥 INIT
# pygame.init()
# pygame.mixer.init()

# # 🎵 MUSIC
# pygame.mixer.music.load("background.mp3")
# pygame.mixer.music.set_volume(0.5)

# # 🔊 SOUNDS
# cut_sound = pygame.mixer.Sound("cut.mp3")
# bomb_sound = pygame.mixer.Sound("bomb.mp3")

# # 🔹 VARIABLES
# player_lives = 3
# score = 0
# fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']

# WIDTH = 800
# HEIGHT = 500
# FPS = 12

# pygame.display.set_caption('Fruit-Ninja Game -- PRO')
# gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()

# WHITE = (255,255,255)

# background = pygame.image.load('back.jpg')
# font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)

# # 🔹 FRUIT GENERATOR
# def generate_random_fruits(fruit):
#     fruit_path = "images/" + fruit + ".png"
#     data[fruit] = {
#         'img': pygame.image.load(fruit_path),
#         'x' : random.randint(100,500),
#         'y' : 800,
#         'speed_x': random.randint(-10,10),
#         'speed_y': random.randint(-80, -60),
#         'throw': random.random() >= 0.75,
#         't': 0,
#         'hit': False,
#     }

# data = {}
# for fruit in fruits:
#     generate_random_fruits(fruit)

# # 🔹 TEXT
# def draw_text(display, text, size, x, y):
#     font = pygame.font.Font(pygame.font.match_font('comic.ttf'), size)
#     text_surface = font.render(text, True, WHITE)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x, y)
#     display.blit(text_surface, text_rect)

# # 🔹 LIVES
# def draw_lives(display, x, y, lives, image):
#     for i in range(lives):
#         img = pygame.image.load(image)
#         display.blit(img, (x + 35*i, y))

# # 🔥 START SCREEN
# def show_start_screen():
#     gameDisplay.blit(background, (0,0))
#     draw_text(gameDisplay, "FRUIT NINJA", 90, WIDTH/2, HEIGHT/4)
#     draw_text(gameDisplay, "Press any key to start", 40, WIDTH/2, HEIGHT/2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             if event.type == pygame.KEYUP:
#                 waiting = False

# # 🔹 GAME OVER SCREEN
# def show_gameover_screen():
#     pygame.mixer.music.stop()
#     gameDisplay.blit(background, (0,0))
#     draw_text(gameDisplay, "GAME OVER", 90, WIDTH/2, HEIGHT/4)
#     draw_text(gameDisplay, f"Score: {score}", 50, WIDTH/2, HEIGHT/2)
#     draw_text(gameDisplay, "Press any key", 40, WIDTH/2, HEIGHT*3/4)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()
#             if event.type == pygame.KEYUP:
#                 waiting = False

# # 🔹 LOOP CONTROL
# first_round = True
# game_over = True
# game_running = True

# # 🎮 MAIN LOOP
# while game_running:

#     if game_over:
#         if first_round:
#             show_start_screen()   # 🔥 START SCREEN
#             first_round = False
#         else:
#             show_gameover_screen()

#         # RESET GAME
#         pygame.mixer.music.play(-1)
#         player_lives = 3
#         score = 0
#         game_over = False

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_running = False

#     gameDisplay.blit(background, (0, 0))

#     score_text = font.render('Score : ' + str(score), True, (255,255,255))
#     gameDisplay.blit(score_text, (0, 0))
#     draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')

#     for key, value in data.items():
#         if value['throw']:
#             value['x'] += value['speed_x']
#             value['y'] += value['speed_y']
#             value['speed_y'] += value['t']
#             value['t'] += 1

#             if value['y'] <= 800:
#                 gameDisplay.blit(value['img'], (value['x'], value['y']))
#             else:
#                 generate_random_fruits(key)

#             mouse = pygame.mouse.get_pos()

#             if not value['hit'] and value['x'] < mouse[0] < value['x']+60 and value['y'] < mouse[1] < value['y']+60:

#                 if key == 'bomb':
#                     bomb_sound.play()
#                     player_lives -= 1

#                     if player_lives <= 0:
#                         game_over = True

#                     img_path = "images/explosion.png"
#                 else:
#                     cut_sound.play()
#                     score += 1
#                     img_path = "images/half_" + key + ".png"

#                 value['img'] = pygame.image.load(img_path)
#                 value['speed_x'] += 10
#                 value['hit'] = True
#         else:
#             generate_random_fruits(key)

#     pygame.display.update()
#     clock.tick(FPS)

# pygame.quit()

import pygame, sys
import os
import random
from pymongo import MongoClient
from datetime import datetime

# 🔥 INIT
pygame.init()
pygame.mixer.init()

# 🎵 MUSIC
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.5)

# 🔊 SOUNDS
cut_sound = pygame.mixer.Sound("cut.mp3")
bomb_sound = pygame.mixer.Sound("bomb.mp3")

# 🔗 MongoDB CONNECT
client = MongoClient("mongodb://localhost:27017/")
db = client["EmoHeal"]
collection = db["scores"]

def save_score(name, score):
    data = {
        "name": name,
        "score": score,
        "datetime": datetime.now()
    }
    collection.insert_one(data)
    print("Score saved ✅")

# 🔹 VARIABLES
player_lives = 3
score = 0
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']

WIDTH = 800
HEIGHT = 500
FPS = 12

pygame.display.set_caption('Fruit-Ninja Game -- PRO')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255,255,255)

background = pygame.image.load('back.jpg')
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)

# 🔹 FRUIT GENERATOR
def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = {
        'img': pygame.image.load(fruit_path),
        'x' : random.randint(100,500),
        'y' : 800,
        'speed_x': random.randint(-10,10),
        'speed_y': random.randint(-80, -60),
        'throw': random.random() >= 0.75,
        't': 0,
        'hit': False,
    }

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

# 🔹 TEXT
def draw_text(display, text, size, x, y):
    font_local = pygame.font.Font(pygame.font.match_font('comic.ttf'), size)
    text_surface = font_local.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)

# 🔹 LIVES
def draw_lives(display, x, y, lives, image):
    for i in range(lives):
        img = pygame.image.load(image)
        display.blit(img, (x + 35*i, y))

# 🔥 START SCREEN
def show_start_screen():
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, "FRUIT NINJA", 90, WIDTH/2, HEIGHT/4)
    draw_text(gameDisplay, "Press any key to start", 40, WIDTH/2, HEIGHT/2)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False

# 🔹 GAME OVER SCREEN
def show_gameover_screen():
    pygame.mixer.music.stop()
    gameDisplay.blit(background, (0,0))
    draw_text(gameDisplay, "GAME OVER", 90, WIDTH/2, HEIGHT/4)
    draw_text(gameDisplay, f"Score: {score}", 50, WIDTH/2, HEIGHT/2)
    draw_text(gameDisplay, "Press any key", 40, WIDTH/2, HEIGHT*3/4)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False

# 🔹 LOOP CONTROL
first_round = True
game_over = True
game_running = True

# 🎮 MAIN LOOP
while game_running:

    if game_over:
        if first_round:
            show_start_screen()
            first_round = False
        else:
            show_gameover_screen()

        # 🔁 RESET GAME
        pygame.mixer.music.play(-1)
        player_lives = 3
        score = 0
        game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    gameDisplay.blit(background, (0, 0))

    score_text = font.render('Score : ' + str(score), True, (255,255,255))
    gameDisplay.blit(score_text, (0, 0))
    draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')

    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']
            value['y'] += value['speed_y']
            value['speed_y'] += value['t']
            value['t'] += 1

            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                generate_random_fruits(key)

            mouse = pygame.mouse.get_pos()

            if not value['hit'] and value['x'] < mouse[0] < value['x']+60 and value['y'] < mouse[1] < value['y']+60:

                if key == 'bomb':
                    bomb_sound.play()
                    player_lives -= 1

                    if player_lives <= 0:
                        save_score("Player1", score)   # 💾 SAVE TO MONGODB
                        game_over = True

                    img_path = "images/explosion.png"
                else:
                    cut_sound.play()
                    score += 1
                    img_path = "images/half_" + key + ".png"

                value['img'] = pygame.image.load(img_path)
                value['speed_x'] += 10
                value['hit'] = True
        else:
            generate_random_fruits(key)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()