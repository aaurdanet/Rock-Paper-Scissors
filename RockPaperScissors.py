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
#input
selection = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

rps = [0, 1, 2]
rps[0] = rock
rps[1] = paper
rps[2] = scissors
#Computer choose
random_selection = random.randint(0, 2)
print("You chose:")
print(rps[selection])

print("Computer chose:")

print(rps[random_selection])

if selection == 0 and random_selection == 0:
    print("Draw")
elif selection == 0 and random_selection == 1:
    print("You lose")
elif selection == 0 and random_selection == 2:
    print("You win")

elif selection == 1 and random_selection == 0:
    print("You win")
elif selection == 1 and random_selection == 1:
    print("Draw")
elif selection == 1 and random_selection == 2:
    print("You lose")

elif selection == 2 and random_selection == 0:
    print("You lose")
elif selection == 2 and random_selection == 1:
    print("You win")
elif selection == 2 and random_selection == 2:
    print("Draw")
