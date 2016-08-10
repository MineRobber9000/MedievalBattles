class Monster:
	def __init__(self, isElf=False):
		self.name = "Monster"
		self.hp = 20
		self.status = []
		self.effectiveness = [1,1,1,1,1,1,1,1]
		self.move = ["Fix code",7,20]
		self.summonSickness = (not isElf)

	def preTurn(self, hasMedicBot=False):
		if "ff" in self.status:
			if self.effectiveness[0] != 0:
				dmg = 3
				if dmg > self.hp:
					dmg = self.hp
				self.hp -= dmg
				print("{!s} is burned by Fire Rat and takes {!s} damage.".format(self.name,dmg))
		if "f" in self.status:
			dmg = self.effectiveness[0]*3
			if dmg > self.hp:
				dmg = self.hp
			self.hp -= dmg
			print("{!s} is burned and takes {!s} damage.".format(self.name,dmg))
		if "p" in self.status:
			dmg = self.effectiveness[6]*2
			while dmg >= self.hp:
				dmg -= 1
			self.hp -= dmg
			print("{!s} is poisoned and takes {!s} damage.".format(self.name,dmg))
		if "v" in self.status:
			dmg = self.effectiveness[6]*2
			if dmg > self.hp:
				dmg = self.hp
			self.hp -= dmg
			print("{!s} was bitten by a Spider-type monster with Venom Bite. The venom deals {!s} damage.".format(self.name,dmg))
		if hasMedicBot:
			if len(self.status) = 0:
				self.hp += 3
				print("The player's Medic Bot heals 3HP for {!s}.".format(self.name))
			else:
				st = self.status.pop()
				if st == "ff":
					stname = "FireRat burn"
				elif st == "f"
					stname = "burn"
				elif st == "p":
					stname = "poison"
				elif st == "v":
					stname = "venom"
				print("The player's Medic Bot heals the {!s} on {!s}.".format(stname,self.name))
		if self.hp <= 0:
			print("{!s} died.".format(self.name))
			return True
		else:
			return False

	def attack(self):
		return self.move

	def attacked(self,move):
		return False # finishing this later.
