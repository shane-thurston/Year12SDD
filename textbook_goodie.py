from character import Character
class Goodie(Character):

  personality = 0
  intelligence = 0

  def __init__(self, fname, agi, hel, per, intl):
    super().__init__(fname, agi, hel)
    if per < 0 or per > 10:
      per = 0
    self.personality = per
    if intl < 0 or intl > 10:
      intl = 0
    self.intelligence = intl

  def details(self):
    print("")
    print("Goodie")
    super().details()
    print("Personality = ",self.personality)
    print("Intelligence =",self.intelligence)
    print("__________________")
