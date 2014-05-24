# Inheritance
#
#

class Animal(object):
    """describes an animal"""
    def __init__(self, name, sound):
        """every animal has a name"""
        self.name = name
        self.sound = sound

    def __str__(self):
        """print the name for the animal"""
        return self.name

    def get_name(self):
        """return the name of the animal"""
        return self.name

    def get_sound(self):
        """return the sound the animal makes"""
        return self.sound

class Cow(Animal):
    """cows are animals that go moo"""

    def __init__(self, name):
        """every cow has a name"""
        super(Cow, self).__init__(name, "mooooo", milk)
        self.milk = milk

    def get_milk(self):
        """every cow gives milk"""
        return self.milk

class Spider(Animal):
    """spiders are animals too"""
    
    def __init___(self, name, message):
        """every spider has a message"""
        super(Spider, self).__init__(name, "tchk, tchk")
        self.message = message

    def get_message(self):
        return self.message
