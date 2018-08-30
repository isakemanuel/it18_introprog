from . import *


class Player:
    def __init__(self, place, inventory=Inventory(), experience=0, health=10):
        self.place = place
        self.inventory = inventory
        self.experience = experience
        self.health = health
        self.finished_quests = []
        self.is_dead = True



    def get_stats(self):
        return "XP: {} --- HP: {}".format(self.experience, self.health)

    def move(self, direction):
        if direction <= len(self.place.borders) and direction > 0:
            self.place = self.place.borders[direction - 1]
            return True
        else:
            return False

    def look_for_quests(self):
        quests_are_available = False
        available_quests = []
        for quest in self.place.quests:
            if quest.can_player_do_quest(player=self):
                quests_are_available = True
                available_quests.append(quest)
        return quests_are_available, available_quests

    def look(self):
        return self.place.description

    def view_inventory(self):
        return self.inventory.view()

    def add_to_inventory(self, item):
        return self.inventory.add_item(item)

    def remove_from_inventory(self, index):
        return self.inventory.remove_item(index)
