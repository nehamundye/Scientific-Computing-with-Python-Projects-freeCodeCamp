import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = [k for k,v in kwargs.items() for i in range(v)]

  def draw(self, numberofballs):
    if numberofballs > len(self.contents):
      temp = self.contents.copy()
      self.contents.clear()
      return temp
    else:
      drawn_balls = random.sample(self.contents, numberofballs)
      for elem in drawn_balls:
        self.contents.remove(elem)
      return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    
    count = 0
    expected_balls_list =[]
    for k,v in expected_balls.items():
        expected_balls_list.append(v)
        for i in range(v):
            if k in balls_drawn:
                balls_drawn.remove(k)
                count += 1

    if count == sum(expected_balls_list):
        success_count += 1
  
  return success_count/num_experiments
