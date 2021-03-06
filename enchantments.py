"""This script has the enchantments class. It will handle all the enchantments and enhancements that the game has"""


class Enchantment:
	"""This is the base class for all weapon enchantments"""
	def __init__(self):
		self.name = "Enchantment"
		self.level = 0
		self.type_affect = "normal"
		self.description = """
A magical spell embedded into your weapon.
This might just come in handy.
		"""
		self.value = 0

	def __str__(self):
		return self.name

	def damage_multiplier(self):
		if self.level == 0:
			damage_multiplier = 1
			return damage_multiplier
		if self.level == 1:
			damage_multiplier = 1.5
			return damage_multiplier
		if self.level == 2:
			damage_multiplier = 2
			return damage_multiplier
		if self.level == 0.5:
			damage_multiplier = 1.2
			return damage_multiplier
		else:
			damage_multiplier = 1.1
			return damage_multiplier


class Hydration(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Hydration"
		self.level = 1
		self.type_affect = ["rock", "fire"]
		self.description = """
This enchantment hydrates all it touches.
I wonder what happens to a wet rock?
		"""
		self.value = 50


class Dehydration(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Dehydration"
		self.level = 1
		self.type_affect = ["water"]
		self.description = """
This enchantment dehydrates all it touches.
I wonder what happens to dry water?
		"""
		self.value = 75


class Extinguishing(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Extinguishing"
		self.level = 1
		self.type_affect = ["fire"]
		self.description = """
This enchantment extinguishes flames. 
Sayonara to all the flames.
		"""
		self.value = 100


class Suction(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Suction"
		self.level = 1
		self.type_affect = ["air"]
		self.description = """
This enchantment sucks in all nearby enemies. 
I wonder what will happen to the air?
		"""
		self.value = 125


class Honed(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Honed"
		self.level = 0.5
		self.type_affect = ["normal", "rock", "fire", "water", "air"]
		self.description = """
This enchantment sharpens your sword. 
Slicing foes is now a piece of cake. 
		"""
		self.value = 100


class Slayer(Enchantment):
	def __init__(self):
		super().__init__()
		self.name = "Human Slayer"
		self.level = 0.5
		self.type_affect = ["human"]
		self.description = """
This enchantment, wants one thing.
Human blood...but who's?
		"""
		self.value = 100
