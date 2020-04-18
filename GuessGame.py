import random


print("welcome to number guess game,there are three levels in the game: easy, medium and hard ")

user_name = input('please your name to begin: ').upper()
user_level = input('choose your desired level: ').lower()



Turns =0
limit = 6
left = 6
while user_level == 'easy' :
    random_number = random.randint(1, 10)
    try:
        Your_guess = input("Enter a number between 1 and 10: ")
        Turns += 1
        left -= 1
        print(f"you have {left} trial(s) left ")
        if Turns == limit:
            print(f'Game 0ver! {user_name}')
            break
        if random_number == int(Your_guess):
            print("You got it right!")
            print("Number of trials you have used: ", Turns)
            break
        else:
            if random_number > int(Your_guess):
                print("that was wrong")
            else:
                print("that was wrong")
    except ValueError:
        print("only integers are allowed")



Turns =0
limit = 4
left = 4
while user_level == 'medium' :
    random_number = random.randint(1, 20)
    try:
        Your_guess = input("Enter a number between 1 and 20: ")
        Turns += 1
        left -= 1
        print(f"{user_name} have {left} trial(s) left ")
        if Turns == limit:
            print(f'Game Over {user_name}')
            break
        if random_number == int(Your_guess):
            print(f"You got it right! {user_name} ")
            print("Number of trials you have used: ", Turns)
            break
        else:
            if random_number > int(Your_guess):
                print("that was wrong")
            else:
                print("that was wrong")
    except ValueError:
        print("only integers are allowed")




Turns =0
limit = 3
left = 3

while user_level == 'hard' :
    random_number = random.randint(1, 50)
    try:
        Your_guess = input("Enter a number between 1 and 50: ")
        Turns += 1
        left -= 1
        print(f"you have {left} trial(s) left ")
        if Turns == limit:
            print(f'Game Over {user_name}')
            break
        if random_number == int(Your_guess):
            print("You got it right!")
            print("Number of trials you have used: ", Turns)
            break
        else:
            if random_number > int(Your_guess):
                print("Number is out of range")
            else:
                print("That was wrong")
    except ValueError:
        print("only integers are allowed")
