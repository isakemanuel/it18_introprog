from model import *


class Game():
    def __init__(self, player, places):

        self.places = places
        self.player = player

    def check_if_done(self):
        if self.player.health == 0:
            print("You died! Game over :(")
            return True
        return False

    def query_player(self):
        #print("\n"*100)

        user_input= input("You are in {}. You can (L)ook around, look for (Q)uests, (V)iew inventory, View (S)tats or (M)ove. What do you want to do?\n".format(self.player.place.name))
        user_input = user_input.upper()
        if user_input == 'M':
            moved = False
            while not moved:
                print("You can move to:")
                print("0: Stay here")
                for index, place in enumerate(self.player.place.borders, 1):
                    print("{}: {}.".format(index, place.name))
                direction = input("Where do you want to move? Enter 0 to stay (enter the number)\n")
                direction = int(direction)
                if direction != 0:
                    moved = self.player.move(direction)
                else:
                    print("You decided to stay.")
                    moved = True
                if not moved:
                    print("Invalid input. You can only enter a number, try again.")

        if user_input == 'Q':
            performed_a_quest = False
            quests_are_available, available_quests = self.player.look_for_quests()
            if quests_are_available:
                print("You can do the following quests:")
                print("0: Do nothing.")
                for index, quest in enumerate(available_quests, 1):
                    print("{}: {}.".format(index, quest.name))
                quest = input("What quest do you want to do? (enter the number) Enter 0 to do nothing\n")
                quest = int(quest)
                if quest != 0:
                    print("You have the following choices:")
                    choices = available_quests[quest - 1].get_quest_prompt()
                    print(choices)
                    user_choice = input("Which do you chose? (enter the number)\n")
                    user_choice = int(user_choice)
                    summary = available_quests[quest - 1].make_choice(index = user_choice-1, player = self.player)
                    print(summary)

                    performed_a_quest = True
                else:
                    print("You decided to do nothing.")
                    performed_a_quest = True
                if not performed_a_quest:
                    print("Invalid input. You can only enter a number, try again.")
            else:
                print("No quests available :(")

        if user_input == 'V':
            for index, item in enumerate(self.player.view_inventory(), 1):
                print("{}: {}.".format(index, item))

            in_inventory = True
            while in_inventory:

                user_input_inv = input("Do you want to (R)emove an item, or just (G)o back?\n")
                user_input_inv = user_input_inv.upper()

                #if user_input_inv == 'A':
                #    item_name = input("what item do you want to add?\n")
                #    print(self.player.add_to_inventory(item_name))


                if user_input_inv == 'R':
                    removing = True
                    while removing:
                        index_number = int(input("what item do you want to remove?\n"))
                        check_remove = input("Are you want remove item number {}: {}? (Y)es or (N)o\n".format(index_number, self.player.view_inventory()[index_number-1]))
                        check_remove = check_remove.upper()
                        if check_remove == 'Y':
                            print(self.player.remove_from_inventory(index_number))
                            removing = False
                        if check_remove == 'N':
                            pass


                if user_input_inv == 'G':
                    in_inventory = False


        if user_input == 'L':
            print(self.player.look())

        if user_input == 'S':
            print(self.player.get_stats())





        print("\n------\n")