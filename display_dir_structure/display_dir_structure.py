import pathlib
import colorama
import os

def display_dir_structure(path, level=0):
    if not os.path.exists(path):
        return print(f'File {path} does not exist')
    
    if not os.path.isdir(path):
        return print(f'Path {path} is not a directory')
    
    path = pathlib.Path(path)
    for item in path.iterdir():
        if item.is_file():
            print(colorama.Fore.GREEN + f'{"   " * level}{item.name}')
        else:
            print(colorama.Fore.BLUE + f'{"   " * level}{item.name}/')
            display_dir_structure(item, level + 1)

    return

display_dir_structure("display_dir_structure")
