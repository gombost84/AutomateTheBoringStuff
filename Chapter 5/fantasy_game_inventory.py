#You are creating a fantasy video game. The data structure to model the player’s inventory will be a
#dictionary where the keys are string values describing the item in the inventory and the value is an
#integer value detailing how many of that item the player has. For example,
#the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#means the player has 1 rope, 6 torches, 42 gold coins, and so on.
#Write a function named displayInventory() that would take any possible “inventory”

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def printInventory(dictionary):
	print('Inventory:')
	item_total = 0
	for i, j in dictionary.items():
		print(j, i)
		item_total += j
	print('Total number of items: ' + str(item_total))


printInventory(inventory)