import pygame
from colours import colour

class button:
  def __init__(self, screen, x, y, text, txt_clr, btn_clr):
    self.screen = screen
    self.x, self.y = x, y
    self.text = text
    self.font = pygame.font.SysFont("freemono", 50)
    self.btn = None # Will be set-up later, after the text is rendered
    self.txt_clr = txt_clr
    self.btn_clr = btn_clr

  def draw(self):
    font = self.font
    btn_text = font.render(self.text, True, self.txt_clr)
    txt_rect = btn_text.get_rect()
    txt_rect.center = (self.x, self.y)
    self.btn = txt_rect
    pygame.draw.rect(self.screen, self.btn_clr, self.btn)
    self.screen.blit(btn_text, self.btn)


def click_btn(button):
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Checks whether the left mouse button is clicked
      left_clicked = pygame.mouse.get_pressed()[0]
      if left_clicked:
          mouse_x, mouse_y = pygame.mouse.get_pos()
          if button != None:
              if button.collidepoint(mouse_x, mouse_y): # Checks if the player clicked the button
                return True