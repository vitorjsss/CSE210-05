from game.scripting.action import Action
from game.casting.actor import Actor
class MoveActorsAction(Action):

    def execute(self, cast, script):
        group = cast.get_all_actors()
        for i in group:
            i.move_next()