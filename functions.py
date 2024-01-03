FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return te list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """Write to-do item list in the next file"""
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_args)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
