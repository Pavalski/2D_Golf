import pygame

pygame.init()

import time
from colours import colour
from ball import golf_ball
from obstacles import Level
from Update_Scores import scores, get_score
from Game_Control import game
from buttons import click_btn
# Set up the screen
WIDTH = 700
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf")
screen.fill(colour.GRASS)

FPS = 60  #Sets the FPS to 60

ball = golf_ball(screen)  #Sets up the golf ball

#Set up fonts
level_font = pygame.font.SysFont("dejavusansmono", 20) 
strks_font = pygame.font.SysFont("dejavuserif", 15)

system = game(screen) #The game system

def main():
    """The main function that runs the game"""
    clock = pygame.time.Clock()
    mouse_down = False
    play = True
    level = Level(screen, ball) # Sets up the levels
    total_strks = 0 #Sets total strokes to 0
    # player_name = input("Enter your name please: ").title() # Gets the player's name
    while play:
        clock.tick(FPS)
        screen.fill(colour.GRASS)
      
        if system.game == "intro": # The title screen
            system.title_scrn()
            if click_btn(system.button):
              system.game = "inst"
        elif system.game == "inst":
          system.inst_scrn()
          if click_btn(system.button):
            system.game = "game"
        elif system.game == "end": # The "Beat the game" screen
            system.end_scrn()
            if click_btn(system.button[0]):
              system.game = "game"
              system.clear_scores()
              total_strks = 0
              level.restart()
            if click_btn(system.button[1]):
              system.game = "bye"
        elif system.game == "bye": # Final goodbye screen
            system.bye_scrn()
            
        elif system.game == "game": # If they are currently playing the game
            #####
            if ball.beat_level: # Checks if the player beat the level
                time.sleep(0.5)  # Adds a pause between levels
                scores(level.level, cur_lvl_strks) # Saves the player's score for the level
                level.level_up()
                if level.level == 19:  #Checks if they beat the game
                    scores(level.level, total_strks)
                    system.game = "end"
            if level.level != level.past_level and level.level != 19: # Starts the level if they didn't beat the game
                level.start_level()
                rcrd_strks = get_score(level.level) # Gets the record for the level
                cur_lvl_strks = 0
            #####
            cur_lvl_txt = level_font.render(f"HOLE {level.level}", True,
                                            colour.RED) #Saves the hole num as text
            total_strks_txt = strks_font.render(
                f"Total Strokes: {total_strks}", True, colour.RED) # Prints the players total strokes as text
            cur_lvl_strks_txt = strks_font.render(f"Strokes: {cur_lvl_strks}",
                                                  True, colour.RED) # Saves the players strokes on the current level as text
            rcrd_strks_txt = strks_font.render(f"Record: {rcrd_strks}", True,
                                               colour.RED) #Prints the record for the hole as text
            #####
            level.draw_level() # Draws the level first so the text goes on top
            # Prints the text in the same order as saved (top-bottom)
            screen.blit(cur_lvl_txt, cur_lvl_txt.get_rect())
            total_strks_rect = total_strks_txt.get_rect()
            total_strks_rect.top = 50
            screen.blit(total_strks_txt, total_strks_rect)
            cur_strks_rect = cur_lvl_strks_txt.get_rect()
            cur_strks_rect.top = 100
            screen.blit(cur_lvl_strks_txt, cur_strks_rect)
            rcrd_strks_rect = rcrd_strks_txt.get_rect()
            rcrd_strks_rect.top = 150
            screen.blit(rcrd_strks_txt, rcrd_strks_rect)
            ######
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: # Resets the user's current stroke
                        if mouse_down:
                            mouse_down = False
                    elif event.key == pygame.K_l: # Level select
                        level_slct = int(input("Level: "))
                        level.level = level_slct
                        level.past_level = level_slct - 1
                if event.type == pygame.MOUSEBUTTONDOWN and ball.vel <= 0:
                    # Checks whether the left mouse button is clicked and the ball isn't moving
                    left_clicked = pygame.mouse.get_pressed()[0]
                    if left_clicked:
                        mouse_down = True
                        mouse_pos1 = pygame.mouse.get_pos()
                        pygame.mouse.get_rel()
                elif event.type == pygame.MOUSEBUTTONUP and mouse_down:
                  #Checks if the mouse is no longer being pressed
                    mouse_move2 = pygame.mouse.get_rel()
                    pygame.mouse.get_pos()
                    if mouse_move2[0] != 0 or mouse_move2[1] != 0: # Checks if the moved the mouse at all
                        ball.start_move(mouse_move2[0], mouse_move2[1])
                        cur_lvl_strks += 1
                        total_strks += 1
                    mouse_down = False
            if mouse_down: # Draws an arrow and power meter if the mouse is being held down
                mouse_pos2 = pygame.mouse.get_pos()
                x, y = mouse_pos2[0] - mouse_pos1[0], mouse_pos2[
                    1] - mouse_pos1[1]
                ball.arrow(x, y)
            if ball.vel > 0:
                ball.moving(level.obsts, level.hole_loc, level.hills,
                            level.surfs)
            ball.draw_ball()
            pygame.display.update()
            if ball.in_water:
                level.ball_strt_loc() # If the ball is in water it goes back to where it started the level
                ball.in_water = False
            elif ball.in_lava == 1: # Lava sends the player back 9 levels
                level.level = 1
                level.past_level = 0
                ball.in_lava = 0
            elif ball.in_lava == 2:
                level.level = 9
                level.past_level = 8
                ball.in_lava = 0


main()
