
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}

print("TASK 1 - SETUP")
print("Yesterday:", yesterday)
print("Today:", today)


new_files = today - yesterday
deleted_files = yesterday - today
print("\nTASK 2 - NEW AND DELETED FILES")
print("New files:", new_files)
print("Deleted files:", deleted_files)

unchanged_files = yesterday & today
print("\nTASK 3 - UNCHANGED FILES")
print("Unchanged files:", unchanged_files)


all_changes = new_files | deleted_files
print("\nTASK 4 - ALL CHANGES")
print("All changed files:", all_changes)

all_files = yesterday | today
print("\nTASK 5 - ALL FILES EVER SEEN")
print("All files:", all_files)


