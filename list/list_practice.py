
shopping_list = ["rice", "milk", "bread", "eggs", "milk", "apples"]
print("TASK 1 - Original shopping list")
print(shopping_list)

print("\nTASK 2 - Accessing list items")
print("Second item:", shopping_list[1])
print("Last item:", shopping_list[-1])
print("Total items:", len(shopping_list))


shopping_list.append("eggs")
print("\nTASK 3 - After appending eggs")
print(shopping_list)

shopping_list.insert(1, "bread")
print("After inserting bread at index 1:")
print(shopping_list)
print("Index explanation: the inserted bread is at index 1; previous items from index 1 onward shift right by 1.")

shopping_list.remove("milk")
print("\nTASK 4 - After removing milk once")
print(shopping_list)

print("\nTASK 5 - Membership and list length")
print('Does "milk" still exist?', "milk" in shopping_list)
print("Items remaining:", len(shopping_list))
print('Yes, "milk" still exists because the original list contained it twice and remove() removes only the first matching item.')
print("Removing one item decreases the list length by 1.")

print("\nTASK 6 - Loop through the shopping list")
for item in shopping_list:
    print(item)
print("Total items after the loop:", len(shopping_list))


removed_item = shopping_list.pop()
print("\nTASK 8 - Remove the last item")
print("Removed item:", removed_item)
print("Updated list:", shopping_list)

unsorted_list = shopping_list.copy()
sorted_list = sorted(shopping_list)
print("\nTASK 9 - Alphabetical sorting")
print("Unsorted copy (unchanged):", unsorted_list)
print("Sorted list:", sorted_list)
