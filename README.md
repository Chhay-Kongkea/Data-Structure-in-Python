# Python Data Structures Practice — Completed

This project completes the exercises in the supplied `python_ds_practice.pdf`.

## Project structure

- `list/list_practice.py` — List tasks (including append, insert, remove, membership, loop, pop, and sorting).
- `tuple/tuple_practice.py` — Student registration and course enrollment.
- `set/set_practice.py` — File comparison using set operations.
- `dictionary/dictionary_practice.py` — Inventory management using dictionary methods.

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## Run

Open a terminal in this project folder and run:

```bash
python list/list_practice.py
python tuple/tuple_practice.py
python set/set_practice.py
python dictionary/dictionary_practice.py
```

On Windows, `py` can be used instead of `python`, for example:

```powershell
py list/list_practice.py
```

## Notes

- The list worksheet skips Task 7 in the supplied PDF; the numbering from the worksheet is preserved.
- `list.remove("milk")` removes only the first matching value, so the second `"milk"` remains.
- Tuples are immutable, so the course tuple is converted to a list, updated, and converted back.
- Set output order is not guaranteed because sets are unordered.
- `dict.setdefault()` does not overwrite a key that already exists.
