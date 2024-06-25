import random
print("Winning rules of the game ROCK PAPER SCISSORS are:\nRock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissors wins \n")
def rps(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    elif choice == 3:
        return 'Scissors'
def winner(user, compu):
    if user == compu:
        return "DRAW"
    elif (user == 1 and compu == 3) or (user == 2 and compu == 1) or (user == 3 and compu == 2):
        return "USER"
    else:
        return "COMPUTER"
user = 0
computer = 0
while True:
    rounds = 3
    for i in range(rounds):
        print("\nEnter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        choice = int(input("Enter your choice: "))      
        while choice > 3 or choice < 1:
            choice = int(input("Enter a valid choice please: "))       
        user_choice= rps(choice)
        print(f"User choice is: {user_choice}")
        comp_choice = random.randint(1, 3)
        computer_choice= rps(comp_choice)
        print(f"Computer choice is: {computer_choice}")
        result = winner(choice, comp_choice) 
        if result == "DRAW":
            print("It's a Draw!")
        elif result == "USER":
            print("You win this round!")
            user += 1
        else:
            print("Computer wins this round!")
            computer += 1   
        print("\nCurrent Scores:")
        print(f"You: {user}")
        print(f"Computer: {computer}")
    print("\nDo you want to play another set of three rounds? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("\nFinal Scores:")
print(f"You: {user}")
print(f"Computer: {computer}")
if user > computer:
    print("You are the overall winner!")
elif computer > user:
    print("Computer is the overall winner!")
else:
    print("It's an overall draw!")
print("Thanks for playing!")