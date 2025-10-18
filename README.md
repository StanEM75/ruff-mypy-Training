# ruff_&_mypy_Training

![Project Image](https://files.realpython.com/media/Showcase-Ruff-Linter_Watermarked.71e600eb11de.jpg)

This is my first project with ruff and mypy.
I want to check how effective these two tools are to correct my code.

---

## 🌿 Branch 1: one_clean_script_one_dirty_script
- `clean_dataset.py`: Clean script
Run ruff check `clean_dataset.py` and mypy `clean_dataset.py` to check the correctness of the code.
- `dirty_dataset.py`: Dirty script
Run ruff check `dirty_dataset.py` and mypy `dirty_dataset.py` to check the correctness of the code.
❗ `dirty_dataset.py` should contain several errors.
  
## 🌿 Branch 2: two_clean_scripts
- `clean_dataset.py`: Clean script
Run ruff check `clean_dataset.py` and mypy `clean_dataset.py` to check the correctness of the code.
- `dirty_dataset_cleaned.py`: Cleaned script
Run ruff check `dirty_dataset.py` and mypy `dirty_dataset.py` to check the correctness of the code.
✅ Should be OK now.




