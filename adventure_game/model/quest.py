class Quest():
    def __init__(self, name="A quest", prompt = "", choices = [], requires_xp = 0, single_try = True):
        self.name = name
        self.prompt = prompt
        self.choices = []
        self.choices += choices
        self.requires_xp = requires_xp
        self.single_try = single_try

    def can_player_do_quest(self, player):
        if self.single_try and self in player.finished_quests:
            return False
        if player.experience < self.requires_xp:
            return False
        return True


    def get_quest_prompt(self):

        return_text = "" + self.prompt
        return_text += "These are your choices:"

        for index, choice in enumerate(self.choices, 1):
            return_text += ("\n{}: {}.".format(index, choice.description))
        return return_text

    def make_choice(self, index, player):
        if self.single_try:
            player.finished_quests.append(self)
        return self.choices[index].perform(player)




    class Choice:
        def __init__(self, description, consequence):
            self.description = description
            self.consequence = consequence


        def perform(self, player):
            self.consequence.perform(player)
            return self.consequence.summary


        class Consequence():
            def __init__(self, health = 0, experience = 0, item = None, summary = ""):
                self.health = health
                self.experience = experience
                self.item = item
                self.summary = summary


            def perform(self, player):
                player.health += self.health
                player.experience += self.experience
                if self.item != None:
                    player.inventory.add_item(self.item)
