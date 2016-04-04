import pygame
import random
import constants
import platforms

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world_x(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    """ Maybe I'll figure this out later
    def shift_world_y(self, shift_y):
        # When the user moves up/down and we need to scroll everything:

        # Keep track of the shift amount
        self.world_shift += shift_y

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y
    """

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Create a wall at the start so you can't go backwards.
        block = platforms.Platform(platforms.WALL) 
        block.rect.x = -150
        block.rect.y = 0
        block.level = self
        self.platform_list.add(block) 
        block = platforms.Platform(platforms.WALL) 
        block.rect.x = -50
        block.rect.y = 0
        block.level = self
        self.platform_list.add(block) 
        block = platforms.Platform(platforms.WALL) 
        block.rect.x = 50
        block.rect.y = 0
        block.level = self
        self.platform_list.add(block)
         

        # Array with type of platform, and x, y location of the platform.
        level = [ # The starting platform
                  [platforms.PLATFORM, 150, 250],
                  [platforms.PLATFORM, 220, 250],
                  [platforms.PLATFORM, 290, 250],
                  # Prevent death of new players.
                  [platforms.PLATFORM, 150, 550],
                  [platforms.PLATFORM, 220, 550],
                  [platforms.PLATFORM, 290, 550],
                  [platforms.PLATFORM, 360, 550],
                  [platforms.PLATFORM, 430, 550],
                  [platforms.PLATFORM, 500, 550],
                  [platforms.PLATFORM, 570, 550],
                  # Learn to jump.
                  [platforms.PLATFORM, 640, 480],
                  [platforms.PLATFORM, 710, 480],
                  [platforms.PLATFORM, 780, 480],
                  [platforms.BLOCK,    640, 550],
                  [platforms.BLOCK,    710, 550],
                  [platforms.BLOCK,    780, 550],
                  # Learn to double jump.
                  [platforms.PLATFORM, 850, 550],
                  [platforms.PLATFORM, 920, 550],
                  [platforms.BLOCK,    990, 550],
                  [platforms.BLOCK,    990, 480],
                  [platforms.BLOCK,    990, 410],
                  [platforms.BLOCK,    990, 340],
                  [platforms.PLATFORM, 990, 270],
                  [platforms.BLOCK,    1060, 550],
                  [platforms.BLOCK,    1060, 480],
                  [platforms.BLOCK,    1060, 410],
                  [platforms.BLOCK,    1060, 340],
                  [platforms.PLATFORM, 1060, 270],
                  [platforms.BLOCK,    1130, 340],
                  [platforms.BLOCK,    1130, 410],
                  [platforms.BLOCK,    1130, 480],
                  [platforms.PLATFORM, 1130, 270],
                  [platforms.BLOCK,    1200, 340],
                  [platforms.PLATFORM, 1200, 270],
                  [platforms.PLATFORM, 1270, 270],
                  # Incase you miss the moving platform.
                  [platforms.PLATFORM, 1270, 480],
                  [platforms.PLATFORM, 1340, 480],
                  [platforms.PLATFORM, 1410, 480],
                  [platforms.PLATFORM, 1480, 480],
                  [platforms.PLATFORM, 1550, 480],
                  [platforms.PLATFORM, 1620, 480],
                  [platforms.PLATFORM, 1690, 480],
                  # After the L/R moving platform
                  [platforms.BLOCK,    2130, -30],
                  [platforms.BLOCK,    2200, -30],
                  [platforms.PLATFORM, 2200, 300],
                  [platforms.BLOCK,    2270, -30],
                  [platforms.BLOCK,    2270, 40],
                  [platforms.PLATFORM, 2270, 300],
                  [platforms.BLOCK,    2340, -30],
                  [platforms.BLOCK,    2340, 40],
                  [platforms.BLOCK,    2400, 110],
                  [platforms.PLATFORM, 2340, 300],
                  [platforms.BLOCK,    2410, -30],
                  [platforms.BLOCK,    2410, 40],
                  [platforms.BLOCK,    2470, 110],
                  [platforms.BLOCK,    2480, -30],
                  [platforms.BLOCK,    2480, 40],
                  [platforms.BLOCK,    2550, 40],
                  [platforms.BLOCK,    2550, -30],
                  [platforms.PLATFORM, 2600, 300],
                  [platforms.PLATFORM, 2670, 300],
                  [platforms.PLATFORM, 2920, 300],
                  [platforms.PLATFORM, 2990, 300],
                  [platforms.PLATFORM, 3060, 300],
                  [platforms.PLATFORM, 3130, 300],
                  ]
        
        # Add a moving platform
        block = platforms.MovingPlatform(platforms.PLATFORM)
        block.rect.x = 1450
        block.rect.y = 200
        block.boundary_left = 1450
        block.boundary_right = 1800
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Create a wall at the start so you can't go backwards.
        block = platforms.Platform(platforms.WALL) 
        block.rect.x = -100
        block.rect.y = 0
        block.level = self
        self.platform_list.add(block)
        block = platforms.Platform(platforms.WALL) 
        block.rect.x = -200
        block.rect.y = 0
        block.level = self
        self.platform_list.add(block)
        
        # Array with type of platform, and x, y location of the platform.
        level = [ # The starting platform
                  [platforms.PLATFORM, 30, 450],
                  [platforms.PLATFORM, 100, 450],
                  [platforms.PLATFORM, 170, 450],
                  [platforms.PLATFORM, 240, 450],
                  # Prevent death of new players.
                  [platforms.PLATFORM, 290, 550],
                  [platforms.PLATFORM, 360, 550],
                  [platforms.PLATFORM, 430, 550],
                  [platforms.PLATFORM, 500, 550],
                  [platforms.PLATFORM, 570, 550],
                  [platforms.PLATFORM, 500, 550],
                  [platforms.PLATFORM, 570, 550],
                  [platforms.PLATFORM, 640, 550],
                  [platforms.PLATFORM, 800, 400],
                  [platforms.PLATFORM, 870, 400],
                  [platforms.PLATFORM, 940, 400],
                  [platforms.PLATFORM, 1000, 500],
                  [platforms.PLATFORM, 1070, 500],
                  [platforms.PLATFORM, 1140, 500],
                  [platforms.PLATFORM, 1120, 280],
                  [platforms.PLATFORM, 1190, 280],
                  [platforms.PLATFORM, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.PLATFORM)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
