import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊📄✂️")

st.title("✊📄✂️ Rock, Paper & Scissors Game")

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

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

user_choice = st.selectbox("Choose your move:", choices)
user_index = choices.index(user_choice)

st.text("Your choice:")
st.code(game_images[user_index])

computer_index = random.randint(0, 2)
st.text("Computer chose:")
st.code(game_images[computer_index])

# Determine the winner
if user_index == computer_index:
    result = "🤝 It's a draw!"
elif (user_index == 0 and computer_index == 2) or      (user_index == 1 and computer_index == 0) or      (user_index == 2 and computer_index == 1):
    result = "🎉 You win!"
else:
    result = "💥 You lose!"

st.subheader(result)