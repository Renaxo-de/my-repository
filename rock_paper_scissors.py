import streamlit as st

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
import random
kamen_skare_papir = ["Rock", "Paper", "Scissors"]

choice = int(input("Što biraš? Napiši 0 za kamen, 1 za papir i 2 za škare \n"))
random_index = random.choice(kamen_skare_papir)

if choice == 0:
    print(rock)
    print("Protivnik je izabrao:")
    if random_index == "Rock":
        print(rock)
        print("Izjednačeno!")
    elif random_index == "Paper":
        print(paper)
        print("Izgubio si!")
    else:
        print(scissors)
        print("Pobijedio si!")


elif choice == 1:
    print(paper)
    print("Protivnik je izabrao:")
    if random_index == "Rock":
        print(rock)
        print("Pobijedio si!")
    elif random_index == "Paper":
        print(paper)
        print("Izjednačeno!")
    else:
        print(scissors)
        print("Izgubio si!")
elif choice == 2:
    print(scissors)
    print("Protivnik je izabrao:")
    if random_index == "Rock":
        print(rock)
        print("Izgubio si!")
    elif random_index == "Paper":
        print(paper)
        print("Pobijedio si!")
    else:
        print(scissors)
        print("Izjednačeno!")
else:
    print("Unos nije valjan.")
