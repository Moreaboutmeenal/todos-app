date = input("Enter todays Date: ")
mood = input("How do you rate your mood today? " )
thoughts = input("Let your thoughts flow: \n")
with open(f"C:/Users/User/Python Projects/Journal/{date}.txt", 'w') as file:
    file.write(mood+2*"\n")
    file.write(thoughts)


