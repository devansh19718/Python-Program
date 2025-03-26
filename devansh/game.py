import random
computer_choices=['rock', 'paper', 'scissor'] 
computer_choice= random.choice(computer_choices) 
user_choice-input()

if user choice not in computer_choices: 
    print("Invalid choice. Pleae choose from rock, paper, or scissor") 
else: 
    If user== choice computer_choice: 
        print("It's a draw") 
        print("Computer choice was:", computer_choice)
         
elif( 
    (user_choice=-'rock' and computer_choice=='scissor') or 
    (user_choice'scissor' and computer choice'paper') and 
    (user_choice'paper' and computer_choice=='rock')
):     
print("You win") 
print("Computer choice was:", computer_choice)

else: 
    print("You lose") 
    print("Computer choice was:", computer_choice)