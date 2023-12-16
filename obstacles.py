import pygame
from colours import colour

class Level:
  def __init__(self, screen, ball):
    self.level = 1
    self.past_level = 0
    self.screen = screen
    self.screenx = pygame.display.get_surface().get_size()[0]
    self.screeny = pygame.display.get_surface().get_size()[1]
    self.ball = ball
    self.obsts = []

  def start_level(self):
    """Sets up the current level"""
    # Set start location for the ball
    self.ball.vel = 0
    self.ball_strt_loc()
    self.obsts = [] # Clears the obstacle list
    self.blocks()
    self.hole()
    self.hill()
    self.spcl_surf()
    self.past_level += 1 # This level has been started

  def draw_level(self):
    """Draws the current level"""
    if len(self.hills) > 0:
      for hill in self.hills:
        pygame.draw.rect(self.screen, colour.BROWN, hill[0])
        self.hill_arrow(hill)
    if len(self.surfs) > 0:
      for surf in self.surfs:
        if surf[1] == "b":
          pygame.draw.rect(self.screen, colour.PINK, surf[0])
        elif surf[1] == "w":
          pygame.draw.rect(self.screen, colour.BLUE, surf[0])
        elif surf[1] == "s":
          pygame.draw.rect(self.screen, colour.SAND, surf[0])
        elif surf[1] == "l":
          pygame.draw.rect(self.screen, colour.LAVA, surf[0])
    if len(self.obsts) > 0:
      for obst in self.obsts:
        pygame.draw.rect(self.screen, colour.DARK_GREEN, obst)
    pygame.draw.circle(self.screen, colour.BLACK, (self.hole_loc[0], self.hole_loc[1]), 8)
    
  def ball_strt_loc(self):
    """Sets the balls starting positions for the level"""
    if self.level == 1:
      # self.ball.set_coor = (self.screenx/2, self.screeny - 100)
      self.ball.x = self.screenx/2
      self.ball.y = self.screeny - 100
    elif self.level == 2:
      self.ball.set_coor(50, self.screeny - 100)
    elif self.level == 3:
      self.ball.set_coor(self.screenx - 100, self.screeny - 100)
    elif self.level == 4:
      self.ball.set_coor(200, 100)
    elif self.level == 5:
      self.ball.set_coor(50, self.screeny - 38)
    elif self.level == 6:
      self.ball.set_coor(45, 545)
    elif self.level == 7:
      self.ball.set_coor(self.screenx - 45, 555)
    elif self.level == 8:
      self.ball.set_coor(self.screenx/2, self.screeny - 50)
    elif self.level == 9:
      self.ball.set_coor(50, 50)
    elif self.level == 10:
      self.ball.set_coor(50,50)
    elif self.level == 11:
      self.ball.set_coor(75, 50)
    elif self.level == 12:
      self.ball.set_coor(25, self.screeny/2)
    elif self.level == 13:
      self.ball.set_coor(50, self.screeny - 50)
    elif self.level == 14:
      self.ball.set_coor(75, 50)
    elif self.level == 15:
      self.ball.set_coor(self.screenx - 50, self.screeny/2 + 80)
    elif self.level == 16:
      self.ball.set_coor(self.screenx - 50, 50)
    elif self.level == 17:
      self.ball.set_coor(self.screenx - 50, self.screeny/2)
    elif self.level == 18:
      self.ball.set_coor(50, self.screeny - 38)
  
  def level_up(self):
    """Adds 1 to the current level"""
    self.level += 1
    # self.level = 12
    self.ball.beat_level = False

  def restart(self):
    self.level = 1
    self.past_level = 0
  
  def blocks(self):
    """Sets up all the blocks in the level"""
    self.obsts = []
    if self.level == 2: # Level 1 doesn't have any blocks
      rect1 = pygame.Rect(self.screenx/2 - 100, self.screeny/2 - 100, 100, 100)
      self.obsts = [rect1]
    elif self.level == 3:
      rect1 = pygame.Rect(100, 100, 100, 100)
      rect2 = pygame.Rect(self.screenx - 200, 200, 50, 50)
      rect3 = pygame.Rect(self.screenx/2 - 75, self.screeny/2 - 75, 75, 75)
      self.obsts = [rect1, rect2, rect3]
    elif self.level == 4:
      rect1 = pygame.Rect(self.screenx/2 - 30, 480, 30, 30)
      rect2 = pygame.Rect(self.screenx/2 - 30, 0, 30, 425)
      self.obsts = [rect1, rect2]
    elif self.level == 5:
      rect1 = pygame.Rect(0, self.screeny - 125, self.screenx - 75, 50)
      rect2 = pygame.Rect(75, self.screeny - 250, self.screenx - 75, 50)
      rect3 = pygame.Rect(0, self.screeny - 375, self.screenx - 75, 50)
      rect4 = pygame.Rect(75, self.screeny - 500, self.screenx - 75, 50)
      self.obsts = [rect1, rect2, rect3, rect4]
    elif self.level == 6:
      rect1 = pygame.Rect(0, 350, 350, 150)
      rect2 = pygame.Rect(350, 0, 350, 265)
      self.obsts = [rect1, rect2]
    elif self.level == 7:
      rect1 = pygame.Rect(self.screenx/2, 425, self.screenx/2, 100)
      rect2 = pygame.Rect(0, 400, 150, 50)
      rect3 = pygame.Rect(0, 175, 150, 50)
      rect4 = pygame.Rect(250, 0, 50, 100)
      rect5 = pygame.Rect(self.screenx - 170, 0, 50, 75)
      rect6 = pygame.Rect(self.screenx - 170, 75, 105, 25)
      self.obsts =[rect1, rect2, rect3, rect4, rect5, rect6]
    elif self.level == 8:
      rect1 = pygame.Rect(0, self.screeny - 150, self.screenx/2 - 50, 50)
      rect2 = pygame.Rect(self.screenx/2 + 50, self.screeny - 150, self.screenx/2 - 50, 50)
      rect3 = pygame.Rect(0, 100, self.screenx/2 - 50, 50)
      rect4 = pygame.Rect(self.screenx/2 + 50, 100, self.screenx/2 - 50, 50)
      self.obsts = [rect1, rect2, rect3, rect4]
    elif self.level == 9:
      rect1 = pygame.Rect(0, 100, 260, 50)
      rect2 = pygame.Rect(self.screenx - 250, 0, 250, 150)
      self.obsts = [rect1, rect2]
    elif self.level == 12:
      rect1 = pygame.Rect(50, 100, 50, 400)
      rect2 = pygame.Rect(100, 100, 500, 50)
      rect3 = pygame.Rect(600, 100, 50, 350)
      rect4 = pygame.Rect(200, 400, 400, 50)
      rect5 = pygame.Rect(150, 200, 50, 250)
      rect6 = pygame.Rect(200, 200, 300, 50)
      rect7 = pygame.Rect(500, 200, 50, 150)
      rect8 = pygame.Rect(250, 300, 250, 50)
      self.obsts = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8]
    elif self.level == 13:
      rect1 = pygame.Rect(500, 0, 50, 40)
      rect2 = pygame.Rect(500, 60, 50, 265)
      rect3 = pygame.Rect(550, 380, 150, 220)
      self.obsts = [rect1, rect2, rect3]
    elif self.level == 14:
      rect1 = pygame.Rect(self.screenx/3, 425, self.screenx/3, 75)
      rect2 = pygame.Rect(75, 350, 30, 75)
      self.obsts = [rect1, rect2]
    elif self.level == 15:
      rect1 = pygame.Rect(150, 100, self.screenx - 250, 50)
      rect2 = pygame.Rect(150, 400, 450, 50)
      self.obsts = [rect1, rect2]
    elif self.level == 16:
      rect1 = pygame.Rect(100, 100, self.screenx - 200, 50)
      self.obsts = [rect1]
    elif self.level == 17:
      rect1 = pygame.Rect(100, 100, 50, self.screeny - 200)
      rect2 = pygame.Rect(self.screenx - 150, 100, 50, self.screeny - 200)
      self.obsts = [rect1, rect2]
      
      
  
  def hole(self):
    """Sets up the location of the hole in the current level"""
    
    if self.level == 1:
      self.hole_loc = (self.screenx/2, 100)
    elif self.level == 2:
      self.hole_loc = (500, 100)
    elif self.level == 3:
      self.hole_loc = (50, 50)
    elif self.level == 4:
      self.hole_loc = (525, 100)
    elif self.level == 5:
      self.hole_loc = (self.screenx - 50, 50)
    elif self.level == 6:
      self.hole_loc = (350/2, 50)
    elif self.level == 7:
      self.hole_loc = (self.screenx - 100, 50)
    elif self.level == 8:
      self.hole_loc = (self.screenx/2, 50)
    elif self.level == 9:
      self.hole_loc = (50, self.screeny - 50)
    elif self.level == 10:
      self.hole_loc = (self.screenx - 50, self.screeny - 50)
    elif self.level == 11:
      self.hole_loc = (30, self.screeny - 50)
    elif self.level == 12:
      self.hole_loc = (490, 275)
    elif self.level == 13:
      self.hole_loc = (self.screenx/2, self.screeny/2)
    elif self.level == 14:
      self.hole_loc = (50, 250)
    elif self.level == 15:
      self.hole_loc = (self.screenx - 25, 50)
    elif self.level == 16:
      self.hole_loc = (self.screenx - 125, 185)
    elif self.level == 17:
      self.hole_loc = (50, self.screeny/2)
    elif self.level == 18:
      self.hole_loc = (self.screenx - 38, 50)
  
  def hill(self):
    """Sets up the location of the hills in the current level. Also, includes the hills direction
    """
    self.hills = []
    if self.level == 4:
      hill1 = pygame.Rect(0, 300, 320, 125)
      hill2 = pygame.Rect(350, 300, self.screenx - 350, 125)
      self.hills = [[hill1, "y", "+"],[hill2, "y", "-"]]
    elif self.level == 5:
      hill1 = pygame.Rect(self.screenx/2, 0, 100, 100)
      self.hills = [[hill1, "x", "+"]]
    elif self.level == 6:
      hill1 = pygame.Rect(250, 500, 100, 100)
      hill2 = pygame.Rect(350, 350, 350, 150)
      hill3 = pygame.Rect(0, 115, 350, 150)
      self.hills = [[hill1, "x", "+"], [hill2, "y", "-"], [hill3, "y", "-"]]
    elif self.level == 7:
      hill1 = pygame.Rect(self.screenx/2, 525, 100, 75)
      hill2 = pygame.Rect(150, 425, 200, 100)
      hill3 = pygame.Rect(self.screenx - 65, 25, 65, 75)
      hill4 = pygame.Rect(150, 100, 150, 125)
      hill5 = pygame.Rect(150, 225, 75, 200)
      hill6 = pygame.Rect(self.screenx - 170, 100, 170, 325)
      hill7 = pygame.Rect(300, 50, 230, 75)
      self.hills = [[hill1, "x", "+"], [hill2, "y", "+"], [hill3, "y", "+"], [hill4, "y", "+"], [hill5, "x", "+"], [hill6, "x", "+"], [hill7, "y", "+"]]
    elif self.level == 8:
      hill1 = pygame.Rect(self.screenx/2 - 50, 75, 100, 75)
      hill2 = pygame.Rect(self.screenx/2 - 50, self.screeny - 150, 100, 75)
      self.hills = [[hill1, "y", "-"], [hill2, "y", "+"]]
    elif self.level == 9:
      hill1 = pygame.Rect(0, 150, self.screenx/2, self.screeny/2 - 100)
      hill2 = pygame.Rect(self.screenx/2, 350, self.screenx/2, self.screeny - 500)
      self.hills = [[hill1, "y", "-"], [hill2, "x", "+"]]
    elif self.level == 11:
      hill1 = pygame.Rect(50, 100, self.screenx/2 - 50, 120)
      hill2 = pygame.Rect(self.screenx/2, 0, self.screenx/2 - 50, 100)
      hill3 = pygame.Rect(self.screenx/2, 100, self.screenx/2 - 50, 350)
      hill4 = pygame.Rect(self.screenx/2, 450, self.screenx/2 - 50, 150)
      self.hills = [[hill1, "y", "-"], [hill2, "y", "-"], [hill3, "x", "+"], [hill4, "y", "+"]]
    elif self.level == 12:
      hill1 = pygame.Rect(0, 100, 50, 60)
      hill2 = pygame.Rect(100, 0, 200, 100)
      hill3 = pygame.Rect(400, 0, 200, 100)
      hill4 = pygame.Rect(600, self.screeny/2 - 30, 50, 60)
      hill5 = pygame.Rect(100, self.screeny/2 - 30, 50, 60)
      hill6 = pygame.Rect(self.screenx/2 - 30, 150, 60, 60)
      hill7 = pygame.Rect(self.screenx/2 - 30, 350, 60, 60)
      self.hills = [[hill1, "y", "-"], [hill2, "x", "+"], [hill3, "x", "+"], [hill4, "y", "+"], [hill5, "y", "-"], [hill6, "x", "+"], [hill7, "x", "-"]]
    elif self.level == 13:
      hill1 = pygame.Rect(0, self.screeny/2, 100, 75)
      hill2 = pygame.Rect(350, 0, 100, 100)
      hill3 = pygame.Rect(550, 175, 150, 75)
      hill4 = pygame.Rect(175, 380, 375, 220)
      self.hills = [[hill1, "y", "-"], [hill2, "x", "+"], [hill3, "y", "+"], [hill4, "y", "+"]]
    elif self.level == 14:
      hill1 = pygame.Rect(self.screenx/3 + 50, 100, self.screenx/3 - 50, 100)
      hill2 = pygame.Rect(self.screenx/3 * 2, 425, self.screenx/3, 75)
      self.hills = [[hill1, "y", "+"], [hill2, "y", "+"]]
    elif self.level == 15:
      hill1 = pygame.Rect(self.screenx - 100, 35, 100, 335)
      self.hills = [[hill1, "y", "-"]]
    elif self.level == 16:
      hill1 = pygame.Rect(0, 200, 75, 250)
      hill2 = pygame.Rect(200, self.screeny - 100, 100, 100)
      self.hills = [[hill1, "y", "-"], [hill2, "x", "+"]]
    elif self.level == 17:
      hill1 = pygame.Rect(0, 100, 100, 100)
      hill2 = pygame.Rect(0, self.screeny - 200, 100, 100)
      self.hills = [[hill1, "y", "+"], [hill2, "y", "-"]]

      
  def hill_arrow(self, hill):
    """Adds an arrow onto the hill to inform the player the slope of the hill"""
    if hill[1] == "x":
      if hill[2] == "+":
        pygame.draw.polygon(self.screen, colour.DARK_BROWN, ((hill[0].left + hill[0].width/4, hill[0].top + hill[0].height/4),(hill[0].left + hill[0].width/4 * 3, hill[0].top + hill[0].height/2), (hill[0].left + hill[0].width/4, hill[0].top + hill[0].height/4 * 3)))
      else:
        pygame.draw.polygon(self.screen, colour.DARK_BROWN, ((hill[0].left + hill[0].width/4 * 3, hill[0].top + hill[0].height/4),(hill[0].left + hill[0].width/4, hill[0].top + hill[0].height/2), (hill[0].left + hill[0].width/4 * 3, hill[0].top + hill[0].height/4 * 3)))
    else:
      if hill[2] == "+":
        pygame.draw.polygon(self.screen, colour.DARK_BROWN, ((hill[0].left + hill[0].width/4, hill[0].top + hill[0].height/4),(hill[0].left + hill[0].width/2, hill[0].top + hill[0].height/4 * 3), (hill[0].left + hill[0].width/4 * 3, hill[0].top + hill[0].height/4)))
      else:
        pygame.draw.polygon(self.screen, colour.DARK_BROWN, ((hill[0].left + hill[0].width/4, hill[0].top + hill[0].height/4 * 3),(hill[0].left + hill[0].width/2, hill[0].top + hill[0].height/4), (hill[0].left + hill[0].width/4 * 3, hill[0].top + hill[0].height/4 * 3)))

  def spcl_surf(self):
    """Sets up any special obstacles that will be in the level"""
    self.surfs = []
    if self.level == 8:
      surf1 = pygame.Rect(self.screenx/2 - 50, self.screeny/2 - 50, 100, 100)
      surf2 = pygame.Rect(50, 200, 50, 50)
      surf3 = pygame.Rect(50, self.screeny - 250, 50, 50)
      surf4 = pygame.Rect(self.screenx - 100, 200, 50, 50)
      surf5 = pygame.Rect(self.screenx - 100, self.screeny - 250, 50, 50)
      self.surfs = [[surf1, "b"], [surf2, "b"], [surf3, "b"], [surf4, "b"], [surf5, "b"]]
    elif self.level == 9:
      surf1 = pygame.Rect(0, self.screeny/2 + 50, self.screenx/4 - 25, 70)
      surf2 = pygame.Rect(self.screenx/2, 150, self.screenx/2, 175)
      surf3 = pygame.Rect(self.screenx/2 + 30, self.screeny - 30, self.screenx/2 - 30, 30)
      surf4 = pygame.Rect(self.screenx/4 + 20, self.screeny/2 + 50, self.screenx/4 - 20, self.screeny/2 - 175)
      surf5 = pygame.Rect(0, self.screeny - 30, self.screenx/2, 30)
      surf6 = pygame.Rect(0, self.screeny/2 + 120, self.screenx/4 - 40, 55)
      surf7 = pygame.Rect(self.screenx/2 + 45, self.screeny/2 + 100, 25, 25)
      self.surfs = [[surf1, "w"], [surf2, "s"], [surf3, "w"], [surf4, "w"], [surf5, "s"], [surf6, "w"], [surf7, "l", 1]]
    elif self.level == 10:
      surf1 = pygame.Rect(self.screenx/2, 0, self.screenx/2, 70)
      surf2 = pygame.Rect(0, 120, self.screenx/2, 70)
      surf3 = pygame.Rect(self.screenx/2, 230, self.screenx/2, 70)
      surf4 = pygame.Rect(0, 325, self.screenx/2, 70)
      surf5 = pygame.Rect(self.screenx/2, 415, self.screenx/2, 70)
      surf6 = pygame.Rect(0, 505, self.screenx/2, 95)
      self.surfs = [[surf1, "w"], [surf2, "w"], [surf3, "w"], [surf4, "w"], [surf5, "w"], [surf6, "w"]]
    elif self.level == 11:
      surf1 = pygame.Rect(0, 0, 50, 450)
      surf2 = pygame.Rect(0, 450, self.screenx/2, 50)
      surf3 = pygame.Rect(50, 220, self.screenx/2 - 50, 230)
      surf4 = pygame.Rect(self.screenx - 50, 0, 50, self.screeny)
      surf5 = pygame.Rect(self.screenx/2 + 75, 230, 50, 50)
      self.surfs = [[surf1, "b"], [surf2, "b"], [surf3, "w"], [surf4, "b"], [surf5, "w"]]
    elif self.level == 12:
      surf1 = pygame.Rect(0, self.screeny - 100, self.screenx, 100)
      self.surfs = [[surf1, "w"]]
    elif self.level == 13:
      surf1 = pygame.Rect(100, 100, 75, self.screeny - 100)
      surf2 = pygame.Rect(175, 100, 325, 75)
      surf3 = pygame.Rect(0, self.screeny/2 - 75, 40, 75)
      surf4 = pygame.Rect(550, 0, 150, 40)
      surf5 = pygame.Rect(550, 250, 65, 30)
      surf6 = pygame.Rect(550, 280, 150, 100)
      surf7 = pygame.Rect(60, self.screeny/2 - 75, 40, 75)
      surf8 = pygame.Rect(635, 250, 65, 30)
      self.surfs = [[surf1, "w"], [surf2, "w"], [surf3, "s"], [surf4, "b"], [surf5, "w"], [surf6, "s"], [surf7, "s"], [surf8, "w"]]
    elif self.level == 14:
      surf1 = pygame.Rect(0, 0, 50, 100)
      surf2 = pygame.Rect(0, 100, self.screenx/3 + 50, 100)
      surf3 = pygame.Rect(self.screenx/3, 0, self.screenx/3, 50)
      surf4 = pygame.Rect(self.screenx/3 * 2, 0, self.screenx/3, 250)
      surf5 = pygame.Rect(self.screenx/3 * 2, 250, self.screenx/3, 100)
      surf6 = pygame.Rect(self.screenx/3, 200, 50, 75)
      surf7 = pygame.Rect(self.screenx/3, 275, 50, 150)
      surf8 = pygame.Rect(0, self.screeny - 50, self.screenx, 50)
      surf9 = pygame.Rect(0, self.screeny - 100, 50, 50)
      surf10 = pygame.Rect(150, self.screeny - 150, 50, 50)
      surf11 = pygame.Rect(105, 350, self.screenx/3 - 105, 75)
      self.surfs = [[surf1, "w"], [surf2, "w"], [surf3, "b"], [surf4, "b"], [surf5, "w"], [surf6, "w"], [surf7, "b"], [surf8, "b"], [surf9, "b"], [surf10, "s"], [surf11, "w"]]
    elif self.level == 15:
      surf1 = pygame.Rect(self.screenx - 150, 150, 50, 300)
      surf2 = pygame.Rect(0, 250, 325, 50)
      self.surfs = [[surf1, "w"], [surf2, "w"]]
    elif self.level == 16:
      surf1 = pygame.Rect(0, 0, 50, 100)
      surf2 = pygame.Rect(75, 165, 475, 335)
      surf3 = pygame.Rect(self.screenx - 100, 100, 100, self.screeny - 100)
      self.surfs = [[surf1, "b"], [surf2, "w"], [surf3, "w"]]
    elif self.level == 17:
      surf1 = pygame.Rect(400, 130, 50, self.screeny - 260)
      surf2 = pygame.Rect(175, 0, 325, 100)
      surf3 = pygame.Rect(175, self.screeny - 100, 325, 100)
      surf4 = pygame.Rect(150, 200, 400, 100)
      surf5 = pygame.Rect(150, 300, 400, 100)
      surf6 = pygame.Rect(225, 100, 50, 50)
      surf7 = pygame.Rect(225, self.screeny - 150, 50, 50)
      self.surfs = [[surf1, "w"], [surf2, "b"], [surf3, "w"], [surf4, "w"], [surf5, "b"], [surf6, "b"], [surf7, "b"]]
    elif self.level == 18:
      surf1 = pygame.Rect(0, self.screeny - 200, self.screenx - 75, 125)
      surf2 = pygame.Rect(self.screenx/2, 200, self.screenx/2, 125)
      surf3 = pygame.Rect(0, 125, self.screenx/2 - 75, 275)
      surf4 = pygame.Rect(0, 0, self.screenx - 75, 125)
      self.surfs = [[surf1, "l", 2], [surf2, "l", 2], [surf3, "l", 2], [surf4, "l", 2]]

  def instructions(self):
    """Shows examples of obstacles for the instructions"""
    
    self.hole_loc = (350, 110)
    rect = pygame.Rect(300, 165, 100, 50)
    self.obsts = [rect]
    hill = pygame.Rect(300, 240, 100, 50)
    self.hills = [[hill, "y", "-"]]
    obst1 = pygame.Rect(300, 315, 100, 50)
    obst2 = pygame.Rect(300, 390, 100, 50)
    obst3 = pygame.Rect(300, 465, 100, 50)
    obst4 = pygame.Rect(300, 540, 100, 40)
    self.surfs = [[obst1, "w"], [obst2, "b"], [obst3, "s"], [obst4, "l"]]