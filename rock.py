import random
cc=["scissor","rock","paper"]
ccs=random.choice(cc)
uc=input()

if uc not in cc:
    print("invalid choice.please select from rock,paper,scissor")
else:
    if uc==ccs:
        print("its draw\n computer_choice was:",ccs)
    elif (uc=='rock' and ccs=='scissor') or (uc=='scissor' and ccs=='paper') or (uc=='paper' and ccs=='rock'):
        print("you win \n computer_choice was:",ccs)
    else:
        print("you lose\n computer_choice was:",ccs)