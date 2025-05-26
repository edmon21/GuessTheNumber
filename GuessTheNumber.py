import random
import pyfiglet

secret_number = random.randint(1, 100) 

attempts = 0
money = 150
attempts_round = 3
pay = 50

title = pyfiglet.figlet_format("Guess The Number")
print(title)

print("Welcome to the Guess the number game!")
print("You will try to guess a number between 1 and 100.")
print("Each round costs 50 dollars.")
print("You have 150 dollars to start with.")
print("If you win, you will earn double what you spent.")
print("If you lose, the next round will cost double the previous one.")

play = input("Do you want to play? (Y/N): ").upper()

if play == "Y":
    print("Let's start!")

    while money >= pay:
        print(f"\nYou have {money} dollars left.")
        print(f"This round costs {pay} dollars. You have {attempts_round} attempts.")
        
        money -= pay
        won = False

        for i in range(attempts_round):
            try:
                guess = int(input("Guess the number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number!")
                won = True
                money += pay * 2
                break

        if not won:
            print(f"You didn't guess the number. It was {secret_number}.")
            pay *= 2

        secret_number = random.randint(1, 100) 

        cont = input("Do you want to continue? (Y/N): ").upper()
        if cont != "Y":
            break

    print(f"\nGame over! You have {money} dollars left.")
else:
    print("Maybe next time!")
