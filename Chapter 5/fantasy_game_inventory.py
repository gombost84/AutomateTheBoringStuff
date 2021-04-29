inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def printInventory(dictionary):
	print('Inventory:')
	item_total = 0
	for i, j in dictionary.items():
		print(j, i)
		item_total += j
	print('Total number of items: ' + str(item_total))


printInventory(inventory)