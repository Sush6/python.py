import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissors]

my_choice=int(input("what do you want to choose?0 for rock, 1 for paper ,2 for scissor\n"))
if my_choice>=0 and my_choice<=2:
    print(images[my_choice])

cmp_choice= random.randint(0,2)
print("computer choice:" + str(cmp_choice))
print(images[cmp_choice])


if my_choice >=3 or my_choice<0:
    print("invalid number")
elif my_choice==0 and cmp_choice==2:
    print("you win")
elif my_choice > cmp_choice:
    print("you win")
elif my_choice < cmp_choice:
    print("you lose")
elif my_choice==cmp_choice:
    print("its a draw")



