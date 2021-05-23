class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, newwidth):
    self.width = newwidth
  
  def set_height(self, newheight):
    self.height = newheight

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2*(self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height **2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ''      
      for h in range(self.height):
        picture += "*" * self.width + '\n'
      return picture
      
  def get_amount_inside(self, othershape):
    return (self.width // othershape.width) * (self.height // othershape.height)
  
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"





class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def set_side(self, newside):
    self.set_width(newside)
    self.set_height(newside)
  
  def __str__(self):
    return f"Square(side={self.width})"