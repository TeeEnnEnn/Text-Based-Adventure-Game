"""This script will have the npc(non player character) classes and will have their attributes"""

import enchantments
import items
import random
import story


class NonPlayerCharacter:
	"""This is the base class for all Non Player Characters (NPC)"""
	def __init__(self):
		self.name = "NonPlayerCharacter"

	def __str__(self):
		return self.name

	@staticmethod
	def generate_inventory(inventory_to_be_filled):
		"""This functions randomly chooses 10 items to be in the trader's inventory"""
		for _ in range(10):
			a = Trader.all_items[random.randint(0, (len(Trader.all_items) - 1))]
			inventory_to_be_filled.append(a)
		return inventory_to_be_filled


class Trader(NonPlayerCharacter):
	"""The trader class is a base class for other classes that interact and trade with the player"""
	all_items = [
		items.SnakeApple(), items.RottenFlesh(), items.CrustyBread(), items.Apple(), items.FreshBread(),
		items.CookedInsectFlesh(), items.HealingPotion(), items.LuckyFruit(), items.StrongHealingPotion(),
		items.HyperHealingPotion(), items.WoodenShield(), items.DefenciveClothing(), items.MetalShield(),
		items.ChainMail(), items.MetalArmour(), items.ReinforcedMetalArmour(), items.ShinySword(), items.LightSaber(),
		items.HeavySaber(), items.BattleAxe(), items.Mace(), items.SharpenedShield(), items.BowAndArrow(),
		items.WoodenClub(), items.MetalClub(), items.Pike(), items.BluntSpear(), items.SharpSpear(), items.Excalibur()
	]

	def __init__(self):
		super().__init__()
		self.name = "Trader"
		self.gold = 250
		self.inventory = [x for x in Trader.all_items if isinstance(x, items.Consumable)]


class Enchanter(NonPlayerCharacter):
	"""This NPC enchants the player's weapons"""
	def __init__(self):
		super().__init__()
		self.name = "Enchanter"
		self.inventory = [
			enchantments.Hydration(), enchantments.Dehydration(), enchantments.Honed(), enchantments.Extinguishing(),
			enchantments.Suction()
		]


class QuestLady(NonPlayerCharacter):
	"""This NPC gives the player a completable quest"""
	def __init__(self):
		super().__init__()
		self.name = "Suspicious Old Woman"
		self.crystals = random.randint(25, 35)
		self.gold = random.randint(15, 85)


class WeaponSmith(Trader):
	"""This NPC trades weapons with the player"""
	def __init__(self):
		super().__init__()
		self.name = "WeaponSmith"
		self.gold = 250
		self.inventory = [x for x in Trader.all_items if isinstance(x, items.Weapon)]


class ArmourSmith(Trader):
	"""This NPC trades armour with the player"""
	def __init__(self):
		super().__init__()
		self.name = "Armour Smith"
		self.gold = 250
		self.inventory = [x for x in Trader.all_items if isinstance(x, items.Defencive)]


class StoryTeller1(NonPlayerCharacter):
	"""Tells the player what they need to do to get out of the cave.
	In particular this NPC tells the player that the cave has 4 main bosses that
	need to be defeated before the player can exit the cave."""
	def __init__(self):
		super().__init__()
		self.name = "Hideous Old Woman"
		self.gold = random.randint(45, 65)
		self.crystals = random.randint(5, 15)
		self.messages = story.storyteller1


class StoryTeller2(NonPlayerCharacter):
	"""This NPC tells the player why they need to defeat the bosses.
	The NPC gives more reason, and explains to the player what really needs to be done."""
	def __init__(self):
		super().__init__()
		self.name = "Quirky Old Timer"
		self.inventory = [Trader.all_items[random.randint(0, 9)]]
		self.messages = story.storyteller2


class StoryTeller3(NonPlayerCharacter):
	"""This NPC is related to the player. This NPC tells the player about the outside world and 
	what the player should expect when they leave the cave."""
	def __init__(self):
		super().__init__()
		self.name = "Mr. Corona"
		self.inventory = [items.MechaDagger(), items.Cash()]
		self.messages = story.storyteller3


class TalkingCharacter(NonPlayerCharacter):
	"""This is the class for random messages to the player"""
	def __init__(self):
		super().__init__()
		self.name = "Random Old Person"
		self.messages = story.random_texts
