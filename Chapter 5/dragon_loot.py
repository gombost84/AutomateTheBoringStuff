#Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing
#the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot.
#The addToInventory() function should return a dictionary that represents the updated inventory.
#Note that the addedItems list can contain multiples of the same item.

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def loottheDagon(inventory, loot):
	for item in loot:
		if item in inventory.keys():
			inventory[item] += 1
		else:
			inventory[item] = 1

def printInventory(dictionary):
	print('Inventory:')
	item_total = 0
	for i, j in dictionary.items():
		print(j, i)
		item_total += j
	print('Total number of items: ' + str(item_total))


loottheDagon(inv, dragonLoot)
printInventory(inv)