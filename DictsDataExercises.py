'''
Created on Jan 24, 2019

@author: darrenbean
'''



#working ex 1
"""
inventory = {
    'rope': 1,
    'torch': 6,
    'gold_coin': 42,
    'dagger': 1,
    'arrow': 12}
"""
def display_inventory(inventory):
    print("Inventory:")
    totalitems = 0
    for k, v  in inventory.items():
        print("{k}:{v}".format(k=k, v=v))
        totalitems = totalitems + v
     
    print("Total items:", totalitems)          

# display_inventory(inventory)


#ex 2

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)
                
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#inv = addToInventory(inv, dragonLoot)
print("Checking old inventory")
display_inventory(inv)
addToInventory(inv, dragonLoot)
print("Checking new inventory")
display_inventory(inv)










        