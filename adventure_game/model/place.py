from . import *

class Place:

    def __init__(self, name=None, description=None, borders = [], secret_borders = [], quests = []):
        self.borders = borders
        self.name = name
        self.description = description
        self.secret_borders = secret_borders
        self.quests = []
        self.quests += quests