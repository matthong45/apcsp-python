# Game of Stones
import random

# global variables
num_stones = 0
# 1 is the human, 2 is the computer
current_turn = 1

# functions
def setup():
    print("Welcome to the Game of Stones!")
    global num_stones
    num_stones = random.randrange(16,21)
    print("We will start out with " + str(num_stones) + " stones.")
    print("You can take 1, 2, or 3 stones in a turn.")
    print("The player who empties the pile wins!")
    global current_turn
    current_turn  = random.randint(1,2)
    tosswinner = ""
    if(current_turn == 1):
        tosswinner = "human"
    else:
        tosswinner = "computer"
    print("The " + tosswinner + " won the coin toss and will play first.")

def computers_turn():
    global num_stones
    amount = num_stones % 4
    # computer can't take zero stones so if the he is in a losing position will take a random number.
    if(amount == 0):
        amount = random.randint(1,3)
    num_stones -= amount
    print("I will take " + str(amount) + " stones.\nSo there are " + str(num_stones) + " left.")

def humans_turn():
    global num_stones
    amount = int(input("Please enter a number of stones between 1 and 3 to take from the pile: "))
    num_stones -= amount
    print("OK, you took " + str(amount) + " stones...\nSo there are " + str(num_stones) + " left.")
    
def check_win():
    global num_stones
    winner = ""
    if(current_turn == 1):
        winner = "human"
    else:
        winner = "computer"

    if num_stones == 0:
        print("The winner was: " + winner)
    
setup()
while num_stones > 0:
    if(current_turn == 2):
      computers_turn()
      check_win()
      current_turn = 1
    else:
      humans_turn()
      check_win()
      current_turn = 2
     
 
 