# Rûn Year 0: A Text Based Adventure
Rûn is fantasy world where elves are the dominant race, with many humans and dwarves living among them.
The world is relitively new to a large form of government, since Kekuel Omah has united the continent
of Jenor under the rule of The First Empire of Jenor. This has stopped many wars, and now it is the 
players turn to journey this world and create thier own story. 

## Pre-Version
As the game stands now, most of what has been done is on the backend, and the game is nothing more
than choosing a class. Soon you will have the ability to travel the world, visit shops, and defeat
enemies...

## The code
This program has been broken up into many small pieces, with the top most parent classes being
located in `run_year0/game_objects/blueprints`. Everything in `run_year0/game_objects` is used for
the main game, and it helps abstract most of what is in `/blueprints`. The `run_year0/world_generation`
is meant to be used to generate the world when the player uploads a save file. 
