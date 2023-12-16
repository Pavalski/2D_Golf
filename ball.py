import pygame
import math
from colours import colour

class golf_ball:
  def __init__(self, screen):
    self.x = 0
    self.y = 0
    self.screen = screen
    self.vel = 0
    self.radius = 5
    self.screenx = pygame.display.get_surface().get_size()[0]
    self.screeny = pygame.display.get_surface().get_size()[1]
    self.beat_level = False
    self.in_water = False
    self.in_lava = 0
  
  def set_coor(self, x, y):
    """Sets the coordinates of the ball"""
    self.x = x
    self.y = y
  
  def draw_ball(self):
    """Draws the ball"""
    pygame.draw.circle(self.screen, colour.WHITE, (self.x, self.y), self.radius)

  def start_move(self, x, y):
    """Sets up the ball to move. Calculates it's velocity"""
    x /= 18 # 20 = 10, 15 = 13 + 1/3
    y /= 18
    power = math.sqrt(x**2 + y**2)
    if power > (11 + 1/9):
      ratio = (11 + 1/9) / power
      power = (11 + 1/9)
      x *= ratio
      y *= ratio
    self.x_vel = x * -1
    self.y_vel = y * -1
    self.vel = power
    self.init_vel = self.vel
    self.stop = 0
    return self.vel

  def moving(self, obstacles, hole_loc, hills, surfs):
    """Main fuction for when the ball is moving. Constrols where it goes and how fast
    """
    if self.vel > 0:
      x_move = (self.vel/self.init_vel) * self.x_vel
      y_move = (self.vel/self.init_vel) * self.y_vel
      if (self.x + x_move + self.radius) >= self.screenx or (self.x + x_move - self.radius) <= 0:
        self.x_vel *= -1
      if (self.y + y_move + self.radius) >= self.screeny or (self.y + y_move - self.radius) <= 0:
        self.y_vel *= -1
      if len(obstacles) > 0:
        self.collide(x_move, y_move, obstacles)
      x_move = (self.vel/self.init_vel) * self.x_vel
      y_move = (self.vel/self.init_vel) * self.y_vel
      if len(surfs) > 0:
        self.spcl_surf(x_move, y_move, surfs)
      if len(hills) > 0:
        self.hill(hills)
      if self.vel > 0.4:
        self.vel -= self.vel * 0.011
      elif not self.hill(hills):
        self.vel = 0
      self.x += x_move
      self.y += y_move  
      self.goal(hole_loc)
      # if self.vel > 0.4:
      #   self.vel -= self.vel * 0.011
      # elif not self.hill(hills):
      #   self.vel = 0
      # print(self.vel)
    return self.vel

  def arrow(self, x, y):
    """Points a line where the ball would go if the mouse was released"""
    x /= 1.25
    y /= 1.25
    power = math.sqrt(x**2 + y**2)
    if power > 160:
      ratio = 160 / power
      power = 160
      x *= ratio
      y *= ratio
    x = self.x + (x * -1)
    y = self.y + (y * -1)
    
    self.power_meter(power)
      
    pygame.draw.line(self.screen, colour.BLACK, (self.x, self.y), (x, y), 3)

  def power_meter(self, power):
    # if self.x <= (self.screenx / 2):
    #   top_right = self.x + 10
    # else:
    #   top_right = self.x - 20
      
    # if self.y >= (self.screeny / 2):
    #   pygame.draw.rect(self.screen, colour.PURPLE, (top_right, self.y - 29, 10, 29), 2)
    #   pygame.draw.rect(self.screen, colour.LIGHT_GREEN, (top_right + 2, self.y - 2 - ((power/160) * 25), 6, (power/160) * 25))
    # else:
    #   pygame.draw.rect(self.screen, colour.PURPLE, (top_right, self.y, 10, 29), 2)
    #   pygame.draw.rect(self.screen, colour.LIGHT_GREEN, (top_right + 2, self.y + 27 - ((power/160) * 25), 6, (power/160) * 25))
    meter = pygame.Surface((50, 200))
    meter.set_alpha(100)
    pygame.draw.rect(meter, colour.PURPLE, meter.get_rect(), 10)
    pygame.draw.rect(meter, colour.LIGHT_GREEN, (10, 190 - ((power/160) * 180), 30, (power/160) * 180))
    self.screen.blit(meter, (0, 400))
  
  def collide(self, x_move, y_move, obstacles):
    """Checks if the ball has collided with a regular block"""
    hit_block = False
    collision_error = 9 # Has a buffer for collisions
    ball_rect = pygame.Rect(self.x - self.radius + x_move, self.y - self.radius + y_move, 10, 10)
    for obstacle in obstacles:
      if (ball_rect).colliderect(obstacle):
        if abs(obstacle.right - ball_rect.left) <= collision_error and self.x_vel < 0:
          self.x_vel *= -1
          hit_block = True
        if abs(obstacle.left - ball_rect.right) <= collision_error and self.x_vel > 0:
          self.x_vel *= -1
          hit_block = True
        if abs(obstacle.top - ball_rect.bottom) <= collision_error and self.y_vel > 0:
          self.y_vel *= -1
          hit_block = True
        if abs(obstacle.bottom - ball_rect.top) <= collision_error and self.y_vel < 0:
          self.y_vel *= -1
          hit_block = True
    return hit_block

  def goal(self, hole_loc):
    """Checks if the ball was hit into the hole with an acceptable velocity"""
    ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 10, 10)
    hole_rect = pygame.Rect(hole_loc[0] - 4, hole_loc[1] - 4, 8, 8) # 8 if the radius of the hole
    if ball_rect.colliderect(hole_rect) and self.vel <= 5:
      self.beat_level = True
      self.vel = 0

  def hill(self, hills):
    """Checks if the ball is on the hill. If it is it adjusts the balls velocity accordinly
    """
    on_hill = False
    ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 10, 10)
    for hill in hills:
      if ball_rect.colliderect(hill[0]):
        if hill[1] == "x":
          if hill[2] == "+":
            if self.x_vel < 0:
              if self.vel > 0.04:
                self.vel += self.vel * 0.013
                if self.vel > (11 + 1/9):
                  self.vel = (11 + 1/9)
              else:
                self.vel = 0.04
            else:
              self.vel -= self.vel * 0.002
            self.x_vel -= 0.2
          else:
            if self.x_vel > 0:
              if self.vel > 0.04:
                self.vel += self.vel * 0.013
                if self.vel > (11 + 1/9):
                  self.vel = (11 + 1/9)
              else:
                self.vel = 0.04
            else:
              self.vel -= self.vel * 0.002
            self.x_vel += 0.2
        else:
          if hill[2] == "+":
            if self.y_vel < 0:
              if self.vel > 0.04:
                self.vel += self.vel * 0.013
                if self.vel > (11 + 1/9):
                  self.vel = (11 + 1/9)
              else:
                self.vel = 0.04
            else:
              self.vel -= self.vel * 0.002
            self.y_vel -= 0.2
          else:
            if self.y_vel > 0:
              if self.vel > 0.04:
                self.vel += self.vel * 0.013
                if self.vel > (11 + 1/9):
                  self.vel = (11 + 1/9)
              else:
                self.vel = 0.04
            else:
              self.vel -= self.vel * 0.002
            self.y_vel += 0.2
        on_hill = True
    return on_hill

  def spcl_surf(self, x_move, y_move, surfs):
    for surf in surfs:
      if surf[1] == "b":
        if self.collide(x_move, y_move, [surf[0]]):
          if self.vel < (7.4): # 7.4074
            self.vel *= 1.5
          else:
            self.vel = (11 + 1/9)
            self.stop += 1
            if self.stop > 8:
              self.vel = 1
      elif surf[1] == "w":
        ball_rect = pygame.Rect(self.x - 3, self.y - 3, 6, 6)
        if (ball_rect).colliderect(surf[0]):
          self.in_water = True
          self.vel = 0
      elif surf[1] == "s":
        ball_rect = pygame.Rect(self.x - self.radius + x_move , self.y - self.radius + y_move, 10, 10)
        if (ball_rect).colliderect(surf[0]):
          self.vel -= self.vel * 0.15
      elif surf[1] == "l":
        ball_rect = pygame.Rect(self.x - 3, self.y - 3, 6, 6)# Makes the collide zone a bit smaller
        if (ball_rect).colliderect(surf[0]):
          self.in_lava = surf[2]
          self.vel = 0
            