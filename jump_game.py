"""
Main module for platform scroller example.
"""

import pygame

import constants
import levels

from player import Player

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Jump Game")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player)) # Not being used currently

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    
    # Starting point for the player
    player.rect.x = 170
    player.rect.y = 200
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Win and lose conditions
    game_over = False
    win = False
    
    # This is a font we use to draw text on the screen (size 100)
    font = pygame.font.Font(None, 100)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done or not game_over:
        
        if player.dead == True:                
                game_over = True
                # If game over is true, draw game over
                text = font.render("Game Over!", True, constants.RED)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 - text_rect.height / 2
                screen.blit(text, [text_x, text_y])

                '''
                # If I decide to add a continue feature (needs to be fixed)
                text = font.render("Continue? Y/N", True, constants.RED)
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                text_y = screen.get_height() / 2 + 30
                screen.blit(text, [text_x, text_y])
                '''

                for event in pygame.event.get(): # User did something
                    if event.type == pygame.QUIT: # If user clicked close
                        done = True # Flag that we are done so we exit this loop
                        
        else:    
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True
                    game_over = True

                if event.type == pygame.KEYDOWN and game_over == False: # User pressed a key
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.go_left()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.go_right()
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.jump()

                if event.type == pygame.KEYUP and game_over == False: # User released a key
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                        player.stop()
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d)and player.change_x > 0:
                        player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 250:
            diff = player.rect.x - 250
            player.rect.x = 250
            current_level.shift_world_x(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 250:
            diff = 250 - player.rect.x
            player.rect.x = 250
            current_level.shift_world_x(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
        # End the game
            game_over = True;
            done = True;
            win = True;
        """ If I add multiple levels
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        """

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # Only draw if the game isn't over
        if game_over == 0:
            current_level.draw(screen)
            active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Update the screen with what we've drawn.
        pygame.display.flip()
        
    # Show victory
    if win == True:
        done = False
        while not done:
            # If game over is true, draw game over
            text = font.render("You Win!", True, constants.BLUE)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        

    # If you forget this line, the program will 'hang' on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
