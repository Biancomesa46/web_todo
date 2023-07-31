def write(item_local, filepath="todos.txt",):
    """Write the todos in to the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(item_local)
    return None

def read_todo(filepath="todos.txt"):
    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
    return local_todos


if __name__ == "__main__":
    print("Nem importált!")