# This file is for the enemies class that will have all of the enemies that will be in the game
class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.hp = 0
        self.damage = 0

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Spider"
        self.hp = 20
        self.damage = 10
        self.defence = 0


class OvergrownInsect(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Overgrown Insect"
        self.hp = 20
        self.damage = 15
        self.defence = 0


class Undead(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Undead"
        self.hp = 30
        self.damage = 10
        self.defence = 0


class SkeletalWarrior(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Skeletal Warrior"
        self.hp = 5
        self.damage = 25
        self.defence = 0


class BatSwarm(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Swarm of Bats"
        self.hp = 20
        self.damage = 15
        self.defence = 0


class Lamia(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Lamia"
        self.hp = 50
        self.damage = 30
        self.defence = 0


# The rock based enemies
class Ogre(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Ogre"
        self.hp = 30
        self.damage = 5
        self.defence = 0


class Golem(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Golem"
        self.hp = 45
        self.damage = 5
        self.defence = 0


class Gargoyle(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Gargoyle"
        self.hp = 30
        self.damage = 10
        self.defence = 0


# The water based enemies
class Hydra(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Hydra"
        self.hp = 30
        self.damage = 10
        self.defence = 0


class WaterNymph(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Water Nymph"
        self.hp = 20
        self.damage = 10
        self.defence = 0


class SeaSerpent(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Sea Serpent"
        self.hp = 25
        self.damage = 12
        self.defence = 0


# The fire based enemies
class BabyPhoenix(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Baby Phoenix"
        self.hp = 10
        self.damage = 25
        self.defence = 0


class Salamander(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Salamander"
        self.hp = 15
        self.damage = 30
        self.defence = 0


class HellHound(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Hell Hound"
        self.hp = 20
        self.damage = 20
        self.defence = 0


# The air based enemies
class Harpy(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Harpy"
        self.hp = 25
        self.damage = 15
        self.defence = 0


class ThunderBird(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Thunder Bird"
        self.hp = 25
        self.damage = 20
        self.defence = 0


class Spriggan(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Spriggan"
        self.hp = 30
        self.damage = 30
        self.defence = 0


# The Boss Enemies
class Geomancer(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Geomancer"
        self.hp = 50
        self.damage = 20
        self.defence = 0


class Hydromancer(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Hydromancer"
        self.hp = 100
        self.damage = 25
        self.defence = 0


class Pyromancer(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Pyromancer"
        self.hp = 150
        self.damage = 30
        self.defence = 0


class Aeromancer(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Aeromancer"
        self.hp = 200
        self.damage = 50
        self.defence = 0