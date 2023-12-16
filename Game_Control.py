import time
from screens import title_screen, end_screen, bye_screen, instructions_screen

class game:
  def __init__(self, screen):
    self.screen = screen
    # self.ball = golf_ball(self.screen)
    self.game = "intro"
    self.file = "curr_player.txt"
    with open(self.file, "w") as f:
      for _ in range(19):
        f.write("0\n")
    self.button = None

  def title_scrn(self):
    self.button = title_screen(self.screen)
    # self.button = end_screen(self.screen, self.file)

  def end_scrn(self):
    self.button = end_screen(self.screen, self.file)

  def bye_scrn(self):
    bye_screen(self.screen)

  def inst_scrn(self):
    self.button = instructions_screen(self.screen)
  
  def clear_scores(self):
    with open(self.file, "w") as f:
      for _ in range(19):
        f.write("0\n")
