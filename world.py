# This file will have the world class. It will deal with the world map, its dynamics and how it can be interacted with
import random
import enemies
import npc


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        This is where your journey begins!
        Will you be the one to save humanity?
        Will you get the answers which you seek?
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        Nothing much happens here.
        """


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ...it grows as you get closer! It's sunlight


        Victory is yours!\n"""


class FindGoldTile(MapTile):
    # Need to find a way to make the gold regenerate, so that you can come back multiple times to get gold
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gold = random.randint(20, 75)
        self.gold_claimed = False

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print(f"+{self.gold} gold added")

    def intro_text(self):
        if self.gold_claimed:
            return """
            Another unremarkable part of the cave.
            You must forge onwards.
            """
        else:
            return """
            Someone dropped some gold.
            You glance to your left and right to make sure no one is watching,
            Then you sneakily pick up the gold.
            """


# Enemy tile types for the element specific tiles
class EnemyTile(MapTile):  # Other enemy tile types will be needed for the area specific enemies
    def __init__(self, x, y):
        r = random.random()
        if r < 0.2:
            self.enemy = enemies.BatSwarm()
            self.alive_text = """
                                A colony of bats fly right above your head.
                                Each looking more blood thirsty than the last.\n
                                """
            self.dead_text = """
                                You have done it.
                                The colony of bats didn't have a chance.\n
                                """
        elif r < 0.4:
            self.enemy = enemies.OvergrownInsect()
            self.alive_text = """
                        A giant centipede sets its eyes on you.
                        Will you make it out alive?\n
            """
            self.dead_text = """
                        The centipede is dead.
                        You fought valiantly, 
                        Its corpse is now your trophy.\n
            """
        elif r < 0.6:
            self.enemy = enemies.SkeletalWarrior()
            self.alive_text = """
                        The rattling of bones. 
                        The hastening of your death?\n
            """
            self.dead_text = """
                        The skeletal warrior is dead.
                        Only its bones remain.\n
            """
        elif r < 0.8:
            self.enemy = enemies.GiantSpider()
            self.alive_text = """
                                A giant spider crawls down from the wall.
                                It stands right in front of you, 
                                You are its prey.\n
            """
            self.dead_text = """
                                The corpse of a dead spider lies before you.
                                Your victory is now certain.\n
                                """
        elif r < 0.99:
            self.enemy = enemies.Undead()
            self.alive_text = """
                                A dead explorer's corpse rises.
                                Will you join him in the dance of death?\n
            """
            self.dead_text = """
                                Can a dead person die again?
                                        Hmm, Maybe?\n
            """

        else:
            self.enemy = enemies.Lamia()
            self.alive_text = """
                                A lamia stands before you.\n
                                Your luck has run out.\n
                                Time to say goodbye.\n
            """
            self.dead_text = """
                                You have escaped death. 
                                You won't be so lucky next time\n
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        # Enemy is attacking the player
        if self.enemy.is_alive():
            try:
                defence_multiplier = 0.1 * player.most_defence().defence
                damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
                player.hp = player.hp - damage_dealt
                print(f"Enemy does {damage_dealt} damage. You have {player.hp} HP remaining")
            except AttributeError:
                player.hp = player.hp - self.enemy.damage
                print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining")


class GeoEnemy(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.33:
            self.enemy = enemies.Ogre()
            self.alive_text = """
                            The ground begins to shake.
                                A blood thirsty Ogre stands before you
                                How long do you have to live?
                                """
            self.dead_text = """
                            The ground is still shaking.
                                But, the Ogre is dead.
                            You must be getting close. 
            """
        elif r < 0.66:
            self.enemy = enemies.Golem()
            self.alive_text = """
                            The ground begins to shake. 
                                Could it be this hunky golem?
            """
            self.dead_text = """
                            The ground is still shaking.
                                The golem is now just a pile of rocks.
                            You must be getting close.
            """
        else:
            self.enemy = enemies.Gargoyle()
            self.alive_text = """
                            The ground begins to shake.
                                The gargoyle sheds its stony surface. 
                                It is ready to attack.
            """
            self.dead_text = """
                            The ground is still shaking.
                                Even its stony skin wouldn't have made a difference
                            You must be getting close.
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                defence_multiplier = 0.1 * player.most_defence().defence
                damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
                player.hp = player.hp - damage_dealt
                print(f"Enemy does {damage_dealt} damage. You have {player.hp} HP remaining")
            except AttributeError:
                player.hp = player.hp - self.enemy.damage
                print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining")


class HydroEnemy(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.33:
            self.enemy = enemies.Hydra()
            self.alive_text = """
                            You begin to hear crashing waves.
                                A hydra stands before you. 
                                All of its eyes looking straight at you.
                                """
            self.dead_text = """
                            The sound of crashing waves intensifies
                                The Hydra is dead and,
                                You have 3 heads to prove it.
                            You must be getting close. 
            """
        elif r < 0.66:
            self.enemy = enemies.WaterNymph()
            self.alive_text = """
                            You begin to hear crashing waves.
                                You have disturbed the waters of a water nymph.
                                You have incurred her wrath.
                            """
            self.dead_text = """
                            The sound of crashing waves intensifies.
                                She did not stand a chance.
                            You must be getting close.
            """
        else:
            self.enemy = enemies.SeaSerpent()
            self.alive_text = """
                                You begin to hear crashing waves.
                                    A Sea serpent, 
                                    Have you just slithered into your death?
                            """
            self.dead_text = """
                            The sound of crashing waves intensifies.
                                Next time you might not be that lucky.
                            You must be getting close.
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                defence_multiplier = 0.1 * player.most_defence().defence
                damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
                player.hp = player.hp - damage_dealt
                print(f"Enemy does {damage_dealt} damage. You have {player.hp} HP remaining")
            except AttributeError:
                player.hp = player.hp - self.enemy.damage
                print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining")


class PyroEnemy(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.33:
            self.enemy = enemies.HellHound()
            self.alive_text = """
                            It's getting hotter by the second.
                                A hell hound of incredible size is before you
                                Has  your luck run out?
                                """
            self.dead_text = """
                            The ground below you is now magma.
                                You turned that hell hound into a puppy.
                                
                            You must be getting close. 
                            
            """
        elif r < 0.66:
            self.enemy = enemies.BabyPhoenix()
            self.alive_text = """
                            It's getting hotter by the second.
                                A phoenix flaps its fiery wings
                                Will you burned along with everything else?
                            """
            self.dead_text = """
                            The ground below you is now magma.
                                You have extinguished the fiery phoenix
                                
                            You must be getting close.
                            
            """
        else:
            self.enemy = enemies.Salamander()
            self.alive_text = """
                                It is getting hotter by the second
                                    A salamander stands before you.
                                    A giant fiery lizard.
                                    Will you be charred? 
                            """
            self.dead_text = """
                            The ground below you is magma.
                                It seems nothing can stop you
                                
                            You must be getting close
                            
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                defence_multiplier = 0.1 * player.most_defence().defence
                damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
                player.hp = player.hp - damage_dealt
                print(f"Enemy does {damage_dealt} damage. You have {player.hp} HP remaining")
            except AttributeError:
                player.hp = player.hp - self.enemy.damage
                print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining")


class AeroEnemy(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.33:
            self.enemy = enemies.Harpy()
            self.alive_text = """
                            The air seems to be getting thinner.
                                Yor mere presence has angered a harpy.
                                You shall face death by its talons
                                """
            self.dead_text = """
                            You can barely breathe now.
                                The harpy has fallen. 
                                You have clipped its once might wings

                            You must be getting close. 

            """
        elif r < 0.66:
            self.enemy = enemies.ThunderBird()
            self.alive_text = """
                            The air seems to be getting thinner.
                                Will you survive its lightning?
                            """
            self.dead_text = """
                            You can barely breathe now
                                The thunderbird is dead. 
                                Hmm, how much do those feathers cost?

                            You must be getting close.

            """
        else:
            self.enemy = enemies.Manticore()
            self.alive_text = """
                                The air is getting thinner.
                                    A winged manticore stands before you.
                                    It is unconquerable.
                            """
            self.dead_text = """
                            You can barely breathe now.
                                You have conquered the unconquerable
                                Could you save humanity?

                            You must be getting close

            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            try:
                defence_multiplier = 0.1 * player.most_defence().defence
                damage_dealt = self.enemy.damage - self.enemy.damage * defence_multiplier
                player.hp = player.hp - damage_dealt
                print(f"Enemy does {damage_dealt} damage. You have {player.hp} HP remaining")
            except AttributeError:
                player.hp = player.hp - self.enemy.damage
                print(f"Enemy does {self.enemy.damage} damage. You have {player.hp} HP remaining")


class TraderTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.trader = npc.Trader()

    def intro_text(self):
        return """
        A frail not-quite human, not-quite creature squats in the corner.
        Clinking his gold coins together. He looks ready to trade.
        """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print(f"{i}.{item.name} - {item.value} Gold")
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ["q", "Q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid Choice\n")

    @ staticmethod
    def swap(seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive for you")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade Complete")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy (S)ell or (Q)uit")
            user_input = input()
            if user_input in ["q", "Q"]:
                return
            elif user_input in ["b", "B"]:
                print("Here is what is available to be bought: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ["s", "S"]:
                print("Here is what can be sold: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid Choice\n")

    # The enchanter will be implemented the same way as the trader


# EN Enemy Tile
# ST start Tile
# VT Victory Tile
# FG Find Gold


world_dsl = """
|TT|FG|EN|EN|FG|TT|TT|FG|EN|EN|FG|TT|
|ST|EN|  |  |EN|  |  |EN|  |  |EN|  |
|EN|FG|EN|  |EN|  |EN|FG|EN|  |EN|  |
|  |EN|  |  |EN|  |  |EN|  |  |EN|  |
|  |EN|  |FG|EN|EN|  |EN|  |FG|EN|EN|
|FG|TT|FG|EN|EN|  |FG|TT|FG|EN|EN|VT|
|TT|FG|EN|EN|FG|TT|TT|FG|EN|EN|FG|TT|
|  |EN|  |  |EN|  |  |EN|  |  |EN|  |
|EN|FG|EN|  |EN|  |EN|FG|EN|  |EN|  |
|  |EN|  |  |EN|  |  |EN|  |  |EN|  |
|  |EN|  |FG|EN|EN|  |EN|  |FG|EN|EN|
|FG|TT|FG|EN|EN|  |FG|TT|FG|EN|EN|VT|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [ln for ln in lines if ln]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}

world_map = []
start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict.get(dsl_cell)
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
