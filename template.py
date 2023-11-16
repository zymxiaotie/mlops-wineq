import os

# create folders:
dirs = [
    os.path.join("data", "raw"), # data/raw,
    os.path.join("data", "processed"), # data/processed,
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs: 
    os.makedirs(dir_, exist_ok=True) # create each folder
    # create .gitkeep in each folder so empty folders can also be pushed to github
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
] 

for file_ in files: 
    with open(file_, "w") as f:
        pass

