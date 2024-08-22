from functions import get_todos,  write_todos
import time
import FreeSimpleGUI

now = time.strftime("%b %d %m %y %H:%M:%S")
print("It is" ,now)

while True:
    user_action = input("Type add show edit or exit complete ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        try:
            todo = user_action[4:]

            todos = get_todos('todos.txt')

            todos.append(todo + '\n')

            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("show"):

        todos = get_todos('todos.txt')

        for index,item in enumerate(todos):
            item = item.title()
            item = item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("complete"):
        try:
            remove = int(user_action[9:])

            todos = get_todos('todos.txt')
            index = remove-1
            todos_remove= todos[index].strip('\n')
            todos.pop(index)

            write_todos('todos.txt', todos)
            message = f"Todo {todos_remove} has been removed from the list"
            print(message)
        except ValueError:
            print("You have entered wrong numberr")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos('todos.txt')

            new_todo = input("Enter a new todo")
            todos[number] = new_todo


            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("exit"):
        break

    else:
        print("Hey you have entered an unknown command, please enter the right command")
print("bye bye!")



