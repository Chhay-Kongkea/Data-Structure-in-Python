
inventory = {
    "rice": 20,
    "milk": 15,
    "bread": 10,
}
print("TASK 1 - INITIAL INVENTORY")
print(inventory)

print("\nTASK 2 - CHECK STOCK WITH get()")
print("Milk stock:", inventory.get("milk", 0))
print("Coffee stock (not found):", inventory.get("coffee", 0))

inventory.update({
    "eggs": 30,
    "apples": 12,
    "rice": 25,
})
print("\nTASK 3 - UPDATE INVENTORY")
print(inventory)

print("\nTASK 4 - PRODUCT STOCK")
for product, stock in inventory.items():
    print(f"{product}: {stock}")

removed_stock = inventory.pop("bread")
print("\nTASK 5 - REMOVE SOLD-OUT PRODUCT")
print("Removed product: bread")
print("Removed stock quantity:", removed_stock)
print("Inventory:", inventory)

inventory.setdefault("oranges", 8)
inventory.setdefault("milk", 999) 
print("\nTASK 6 - ADD PRODUCT WITH setdefault()")
print(inventory)


total_stock = sum(inventory.values())
print("\nTASK 7 - TOTAL ITEMS IN STOCK")
print("Total stock:", total_stock)

backup_inventory = inventory.copy()
inventory.clear()
print("\nTASK 8 - BACKUP AND CLEAR")
print("Original inventory after clear():", inventory)
print("Backup inventory:", backup_inventory)
