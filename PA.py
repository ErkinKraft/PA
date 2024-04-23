import argparse
import ast

def get_imported_libraries(file_name):
    with open(file_name, 'r') as file:
        tree = ast.parse(file.read())
        imported_libraries = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported_libraries.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imported_libraries.add(node.module)
        return imported_libraries

def generate_pyinstaller_command(file_name, onefile, noco, icon, imported_libraries):
    command = f"pyinstaller {file_name}"
    if onefile:
        command += " --onefile"
    if noco:
        command += " --noconsole"
    if icon:
        command += f" --icon {icon}"
    for lib in imported_libraries:
        command += f" --hidden-import {lib}"
    return command

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="Name of the Python file")
    parser.add_argument("--onefile", action="store_true", help="Flag for --onefile option")
    parser.add_argument("--noconsole", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--noco", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--nc", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--noc", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--nconsole", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--of", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--ofile", action="store_true", help="Flag for --noconsole option")
    parser.add_argument("--icon", type=str, help="Icon file name")
    parser.add_argument("--ico", type=str, help="Icon file name")
    parser.add_argument("--ic", type=str, help="Icon file name")
    args = parser.parse_args()

    imported_libraries = get_imported_libraries(args.file_name)
    command = generate_pyinstaller_command(args.file_name, args.onefile, args.noco, args.icon, imported_libraries)
    print(command)

if __name__ == "__main__":
    main()
