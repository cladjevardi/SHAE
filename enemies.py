"""
Module for enemies.
"""
import pygame

from spritesheet_functions import SpriteSheet

# These constants define our enemy types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

""" Animation for enemy (not sure where to put it yet)
# The animated walk left/right of the enemy
enemy_frames_l = []
enemy_frames_r = []
enemy_sheet = SpriteSheet("enemy1.png")

# Load all enemy right facing images into a list
image = enemy_sheet.get_image(0, 0, 60, 60)
self.enemy_frames_r.append(image)
image = enemy_sheet.get_image(63, 0, 60, 60)
self.enemy_frames_r.append(image)
image = enemy_sheet.get_image(126, 0, 60, 60)
self.enemy_frames_r.append(image)

# Load all enemy right facing images into a list, then flip to face left
image = enemy_sheet.get_image(0, 0, 60, 60)
image = pygame.transform.flip(image, True, False)
self.enemy_frames_r.append(image)
image = enemy_sheet.get_image(63, 0, 60, 60)
image = pygame.transform.flip(image, True, False)
self.enemy_frames_r.append(image)
image = enemy_sheet.get_image(126, 0, 60, 60)
image = pygame.transform.flip(image, True, False)
self.enemy_frames_r.append(image)
"""

ENEMY = (0, 0, 60, 60)

class Enemy(pygame.sprite.Sprite):
    """ Static Hazard object the user can collide with """

    def __init__(self, sprite_sheet_data):
        """ Hazard constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            cod. """
        pygame.sprite.Sprite.__init__(self)

        enemy_sheet = SpriteSheet("enemy1.png")
        # Grab the image for this enemy
        self.image = enemy_sheet.get_image(enemy_sheet_data[0],
                                            enemy_sheet_data[1],
                                            enemy_sheet_data[2],
                                            enemy_sheet_data[3])
        self.rect = self.image.get_rect()        

class MovingEnemy(Enemy):
    """ This is a moving enemy. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the enemy.
            If the player is in the way, it will kill the player."""
        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # This should kill the player
            player.dead = True

        # Move up/down
        self.rect.y += self.change_y

        """ If we want we can add this code to make the enemy die
                when landed on (requires editting)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
        """

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
