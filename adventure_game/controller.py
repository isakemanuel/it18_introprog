from game import *
from model import *



#Create places to lay out the foundation of the world

places = {
    "tgh" : Place(name="The Great Hall", description="It's a hall and it's great"),
    "tsh" : Place(name="The Small Hall", description="It's a hall and it's small"),
    "td" : Place(name="The Dungeon", description="It's dungeon and you see two ways out of here")
}

#Establish relationship between different places to enable the player to move between them

places.get("tgh").borders = [places.get("tsh")]
places.get("tsh").borders = [places.get("tgh"), places.get("td")]
places.get("td").borders = [places.get("tsh")]


#Create quests which the player can perform

quest1 = Quest(
    name="The First Quest",
    prompt="Oh no, blablablablablabla? What is your next course of action???",
    choices=[
        Quest.Choice(
            description="Run!!",
            consequence=Quest.Choice.Consequence(
                health=-5,
                summary="Not much happened. You got a bit tired and lost 5 HP."
            )
        )
    ]
)




#Add quests to places
places.get("tgh").quests.append(quest1)

#Create the player
player = Player(place=places.get("tgh"))

#Initialize game with the player and the places created above
game = Game(player=player, places = places)
done = False

#Run game loop
while not done:
    game.query_player()
    done = game.check_if_done()


