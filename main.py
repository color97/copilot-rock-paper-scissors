# Write a rock, paper, scissors game
# import random module
import random
# define main function that handles all the logic
def main():
    # create a list of possible choices
    choices = ['rock', 'paper', 'scissors']
    # get user input
    user_choice = input('Enter rock, paper, or scissors: ')
    # get computer choice
    computer_choice = random.choice(choices)
    # print computer choice
    print(f'Computer choice: {computer_choice}')
    # determine the winner
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
    else:
        print('You lose!')
        
# call main function ↩️

main()