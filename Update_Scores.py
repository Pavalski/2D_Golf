files = ["High_Scores.txt", "curr_player.txt"]

def scores(level, strokes):
  for file in files:
    with open(file, "r+") as f:
      scores_lst = list(map(str.rstrip, f.readlines()))
      if file == files[0]:
        if strokes < int(scores_lst[level - 1]) or int(scores_lst[level - 1]) == 0:
          scores_lst[level - 1] = str(strokes)
          # with open("High_Score_Holders.txt", "r+") as f2:
          #   holders_lst = list(map(str.rstrip, f2.readlines()))
          #   holders_lst[level - 1] = player_name
          #   f2.truncate(0)
          #   f2.seek(0)
          #   for holder in holders_lst:
          #     f2.write(holder + "\n")
      else:
        scores_lst[level - 1] = str(strokes)
      f.truncate(0)
      f.seek(0)
      for score in scores_lst:
        f.write(score + "\n")

def get_score(level):
  with open("High_Scores.txt", "r") as f:
    cur_score = list(map(str.rstrip, f.readlines()))[level - 1]
    return cur_score