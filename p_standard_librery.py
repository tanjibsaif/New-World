# #Working_with_path_2
# from pathlib import Path

# path=Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path=path.with_suffix(".txt")
# print(path)


# #Working_with_directories_3
# from pathlib import Path
# path=Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# print(path.resolve())

# paths=[p for p in path.iterdir() if p.is_dir()]
# py_file=[p for p in path.glob("*.py")]
# print(py_file)

from pathlib import Path
path=Path("scom/__init__.py")
print(path.stat())