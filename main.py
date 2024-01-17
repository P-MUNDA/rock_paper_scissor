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

#Write your code below this line 👇
import random
computer_choice=random.randint(0,2)
symbol=[rock,paper,scissors]
your_choice=int(input("Whay is you choice? 0 for rock,1 for paper and 2 for scissors \n"))

print(f"computer choice is: {symbol[computer_choice]}")
if your_choice==0 or your_choice==1 or your_choice==2:
    print(f"your choice is: {symbol[your_choice]}")  
else:
  print("Wrong entry")

if computer_choice>your_choice:
 if computer_choice==2 and your_choice==0:
  print("You win")
 else:
   print("You lose")
elif computer_choice==your_choice:
  print("It's a tie")

elif computer_choice<your_choice and your_choice<=2:
  print("You win")
elif computer_choice<your_choice and your_choice>2:
  print("Wrong enty ! You lose")
else:
  print("You entered a invalid entry.You lose! you fool")

  