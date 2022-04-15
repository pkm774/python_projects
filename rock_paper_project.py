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

# Write your code below this line 👇

random_no = random.randint(0, 2)

print(f'what do you choose?, 0 for rock, 1 for paper, 2 for scissor')
input_no = int(input("Enter your choice: "))

choice = [rock, paper, scissors]
h_selection = choice[input_no]
ai_selection = choice[random_no]

print(f'You choose {h_selection}')
print(f'computer choose {ai_selection}')

if (h_selection == paper) and (ai_selection == rock):
    print('Human Win this match')
elif (h_selection == scissors) and (ai_selection == paper):
    print('Human Win this match')
elif (h_selection == rock) and (ai_selection == scissors):
    print('Human Win this match')
elif h_selection == ai_selection:
    print('Draw between human and computer !')
else:
    print('Human lost this match')
