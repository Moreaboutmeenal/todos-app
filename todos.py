while True:
    choice = int(input("What would you like to do?" "\n"
                   "1- Add new todo to the last list" "\n"
                   "2- Create a New todo list" "\n"
                   "3- Delete the last todo list""\n"
                   "4- Edit the last list""\n"))

    match choice:

        case 2:

            no_todos = int(input("Enter the no of todos you want to add"))
            todos = []
            for i in range (0,no_todos):
                print("enter the todo", i+1)
                todo = input("")
                print("Todo Number", i+1,"is", todo )
                todos.append(todo)
                file = open('todos.txt', "w")

                file.writelines(todos)

                file.close()

        case 1:
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todo = input("enter the new todo")
            todos.append(new_todo)

        case 3:
            todos =[]
            file= open('todos.txt','r')
            todos = file.read()

    print(todos)











