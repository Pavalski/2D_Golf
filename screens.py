import pygame
from colours import colour
from buttons import button
from obstacles import Level

def title_screen(screen):
  """Creates the title screen for the start of the game"""
  #Draws an image for the title screen
  pygame.draw.circle(screen, colour.BLACK, (550, 475), 30)
  pygame.draw.polygon(screen, colour.RED, ((550, 100), (675, 145), (550, 190)))
  pygame.draw.line(screen, colour.GREY, (550, 500), (550, 100), 30)
  pygame.draw.circle(screen, colour.WHITE, (525, 500), 50)
  #Sets up the font that will be used
  font = pygame.font.SysFont("freemono", 100)
  font.set_bold(True)
  #Writes the title GOLF
  title_txt = font.render("GOLF", True, colour.BLACK)
  title_rect = title_txt.get_rect()
  title_rect.center = (350, 200)
  screen.blit(title_txt, title_rect)
  #Sets up the play button
  title_button = button(screen, 340, 375, "PLAY", colour.WHITE, colour.BLACK)
  title_button.draw()
  pygame.display.update()
  return title_button.btn
  
def end_screen(screen, file):
  """Creates the end screen"""
  #Sets up the font
  font = pygame.font.SysFont("freemono", 20)
  font.set_bold(True)
  #Writes the scores the player got
  with open(file, "r") as f:
    scores = list(map(str.rstrip, f.readlines()))
    # print(scores)
    for level, score in enumerate(scores):
      if (level + 1) != 19:
        txt = font.render(f"Level {level + 1}: {score}", True, colour.BLACK)
      else:
        txt = font.render(f"Total Score: {score}", True, colour.BLACK)
      txt_rect = txt.get_rect()
      if level in range(0, 6):
        txt_rect.topleft = (10, (level * 75) + 10)
      elif level in range(6, 12):
        txt_rect.topleft = (275, ((level - 6) * 75) + 10)
      elif level in range(12, 18):
        txt_rect.topright = (690, ((level - 12) * 75) + 10)
      elif level == 18:
        txt_rect.center = (350, 470)
      screen.blit(txt, txt_rect)
  ply_agn_txt = font.render("Play Again?", True, colour.WHITE)
  ply_agn_txt_rect = ply_agn_txt.get_rect()
  ply_agn_txt_rect.center = (100, 550)
  pygame.draw.rect(screen, colour.BLACK, ply_agn_txt_rect)
  screen.blit(ply_agn_txt, ply_agn_txt_rect)
  btn_rects = []
  yes_btn = button(screen, 300, 550, "YES", colour.WHITE, colour.GREEN)
  yes_btn.draw()
  btn_rects.append(yes_btn.btn)
  no_btn = button(screen, 500, 550, "NO", colour.WHITE, colour.RED)
  no_btn.draw()
  btn_rects.append(no_btn.btn)
  pygame.display.update()
  return btn_rects

def bye_screen(screen):
  """Final Screen"""
  font = pygame.font.SysFont("freemono", 145)
  font.set_bold(True)
  bye_txt1 = font.render("Thanks", True, colour.BLACK)
  bye_txt1_rect = bye_txt1.get_rect()
  bye_txt1_rect.center = (350, 150)
  screen.blit(bye_txt1, bye_txt1_rect)
  bye_txt2 = font.render("For", True, colour.BLACK)
  bye_txt2_rect = bye_txt2.get_rect()
  bye_txt2_rect.center = (350, 300)
  screen.blit(bye_txt2, bye_txt2_rect)
  bye_txt3 = font.render("Playing", True, colour.BLACK)
  bye_txt3_rect = bye_txt3.get_rect()
  bye_txt3_rect.center = (350, 450)
  screen.blit(bye_txt3, bye_txt3_rect)
  pygame.display.update()

def instructions_screen(screen):
  """Instruction Screen"""
  font = pygame.font.SysFont("freemono", 14)
  txt_lst = []
  stroke_txt = font.render("Left click, pull back then release to hit the ball. Right click to reset the hit.", True, colour.BLACK)
  txt_lst.append(stroke_txt)
  hole_txt = font.render("Your aim is to get the ball into this hole. There is a speed limit.", True, colour.BLACK)
  txt_lst.append(hole_txt)
  block_txt = font.render("Regular Block: The ball bounces of it", True, colour.BLACK)
  txt_lst.append(block_txt)
  hill_txt = font.render("Hill: A steep hill, the arrow points uphill.", True, colour.BLACK)
  txt_lst.append(hill_txt)
  water_txt = font.render("Water: Makes the ball go back to where it started the current level.", True, colour.BLACK)
  txt_lst.append(water_txt)
  bounce_txt = font.render("Bouncy Block: When the ball bounces of it, it gains speed", True, colour.BLACK)
  txt_lst.append(bounce_txt)
  sand_txt = font.render("Sand: Drastically slows down the ball.", True, colour.BLACK)
  txt_lst.append(sand_txt)
  lava_txt = font.render("Lava: Found on levels 9 and 18, send you back 9 levels.", True, colour.BLACK)
  txt_lst.append(lava_txt)
  levels_txt = font.render("There are 18 levels! Have fun, enjoy!", True, colour.BLACK) 
  txt_lst.append(levels_txt)

  for txt_num, txt in enumerate(txt_lst):
    if txt_num == 0:
      rect = txt.get_rect()
      rect.topleft = (25, 10)
    elif txt_num == len(txt_lst) - 1:
      rect = txt.get_rect()
      rect.bottomleft = (75, 600)
    else:
      rect = txt.get_rect()
      rect.center = (350, 75 * txt_num)
    screen.blit(txt, rect)

  pygame.draw.circle(screen, colour.WHITE, (350, 45), 5) #Fake ball
  inst_lvl = Level(screen, None)
  inst_lvl.instructions()
  inst_lvl.draw_level()

  cont_button = button(screen, 560, 575, "Continue", colour.GREEN, colour.BLACK)
  cont_button.draw()
  pygame.display.update()
  return cont_button.btn