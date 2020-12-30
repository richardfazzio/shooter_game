import sys
import pygame
import os
import json
import random as rand
from sprites import Sprite

# Get texts from json file
with open('./assets/resources_master/texts.json') as texts_file:
    texts = json.load(texts_file)

# Get asset paths from json
with open('./assets/resources_master/paths.json') as paths_file:
    paths = json.load(paths_file)

# Constants
SPEED = 3
MAX_RIGHT = 685
MAX_LEFT = 6
MAX_TOP = 6
MAX_BOTTOM = 680
FPS = 60

# globals
projectiles = []

pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption(texts.get('window_title'))
size = width, height = 720, 720

screen = pygame.display.set_mode(size)

Background = Sprite(paths.get('game_background_1'), [0, 0])

# Load image assets
character_1_up = pygame.image.load(paths.get('character_1_up'))
character_1_right = pygame.image.load(paths.get('character_1_right'))
character_1_down = pygame.image.load(paths.get('character_1_down'))
character_1_left = pygame.image.load(paths.get('character_1_left'))

enemy_projectile = pygame.image.load(paths.get('enemy_projectile'))
player_projectile = pygame.image.load(paths.get('player_projectile'))

character = character_1_right
starting_height = height / 2
starting_width = width / 2

character_rect = character_1_right.get_rect(topleft=(starting_height, starting_width))


class Projectile:
    def __init__(self, origin, direction, harmful=True):
        """

        :param origin: Initial location of the projectile
        :param direction: Equal to the direction the projectile is traveling
        :param harmful: If False implies is an allied bulley
        """
        # self.direction = direction
        self.harmful = harmful
        self.location = enemy_projectile.get_rect()
        self.projectile_sprite = character_1_down if harmful else character_1_up
        self.direction = direction

    def move_projectile(self):
        print('moving...')


class Character:
    alive = True  # If False means the character is dead

    def __init__(self, character_sprite, location, facing=1, is_player=False):
        """

        :param character_sprite: pygame image
        :param location: pygame get_rect
        :param facing: 0-3 indicating which way the character is facing, 0 is up incrementing clockwise
        :param is_player: is used to determine is the character is the player or not, if False implies is an enemy
        """
        """

        """
        self.character_sprite = character_sprite
        self.location = location
        self.is_player = is_player
        self.facing = facing

    def shoot(self):
        print('Shoot')
        harmful = False if self.is_player else True
        return Projectile(origin=self.location, direction=self.facing, harmful=harmful)


class PlayerCharacter(Character):
    score: 0

    def killed_enemy(self):
        self.score += 1


# Enemy = Character(character, character_rect)
Player = PlayerCharacter(character, character_rect, 1, True)
new_one = PlayerCharacter(character, character_rect, 1, True)
while True:
    clock.tick(60)

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Character turning
    if keys[pygame.K_LEFT] \
            and not keys[pygame.K_RIGHT] \
            and not keys[pygame.K_UP] \
            and not keys[pygame.K_DOWN]:
        Player.character_sprite = character_1_left
    elif keys[pygame.K_RIGHT] \
            and not keys[pygame.K_LEFT] \
            and not keys[pygame.K_UP] \
            and not keys[pygame.K_DOWN]:
        Player.character_sprite = character_1_right
    elif keys[pygame.K_UP] \
            and not keys[pygame.K_LEFT] \
            and not keys[pygame.K_RIGHT] \
            and not keys[pygame.K_DOWN]:
        Player.character_sprite = character_1_up
    elif keys[pygame.K_DOWN] \
            and not keys[pygame.K_LEFT] \
            and not keys[pygame.K_RIGHT] \
            and not keys[pygame.K_UP]:
        Player.character_sprite = character_1_down

    # Character movements
    if keys[pygame.K_a]:
        if character_rect.left > MAX_LEFT:
            Player.location.left -= SPEED
    if keys[pygame.K_s]:
        if character_rect.top < MAX_BOTTOM:
            Player.location.top += SPEED
    if keys[pygame.K_d]:
        if character_rect.left < MAX_RIGHT:
            Player.location.left += SPEED
    if keys[pygame.K_w]:
        if character_rect.top > MAX_TOP:
            Player.location.top -= SPEED

    # Shoot
    if keys[pygame.K_SPACE]:
        screen.blit(new_one.character_sprite, new_one.location)
    # for projectile in projectiles:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(Background.image, Background.rect)
    screen.blit(Player.character_sprite, Player.location)
    screen.blit(new_one.character_sprite, new_one.location)
    pygame.display.flip()
