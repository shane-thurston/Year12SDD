class Character:
  name = ''
  agility = 0
  health = 0
  
  def __init__(self, fname, agi, hel):
    self.name = fname
    self.agility = self.set_agility(agi)
    self.health = hel

  def set_agility(self,a):
    if a < 0 or a > 10:
      a = 0
    return a

  #This is the print() method from textbook  
  def details(self):
    print("My name is",self.name)
    print("Agility =",self.agility)
    print("Health =",self.health)
