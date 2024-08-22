def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(filepath, todo_arg):
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
