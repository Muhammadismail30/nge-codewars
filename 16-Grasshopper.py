class Hero(object):
    def __init__(self, name, experience=0, health=100, position='00', damage=5):
        #Add default values here
        self.name = 'Hero'
        self.experience= experience
        self.health = health
        self.position = position
        self.damage = damage


Hero2 = Hero()
Hero2.name()
