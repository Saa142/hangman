import sys
import random
name = input("What is your name?\n")
def play():
  print(f"Hello, {name}, let's play hangman!")
  print("Start guessing...")
  #Defining words
  wordsList = ["simon","fraser", "university", "vancouver", "computer", "science", "programming", "raincouver", "coquitlam", "burnaby", "newyear", "holiday", "parameters", "canada", "persian", "alexa"]
  word = random.choice(wordsList)
  guesses = " "
  turns = 10
  while turns > 0:
    failed = 0
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        failed += 1
    if failed == 0:
      print("YAY! You win!")
      choice = input("Would you like to play again? y/n\n")
      if "y" in choice:
        play()
      elif "n" in choice:
        sys.exit()
      else:
        print("Error: Invalid response, type y or n.")
    guess = input("Guess a character:")
    guesses += guess
    if guess not in word:
      turns -= 1
      print("Wrong!")
      print(f"You have {turns} more guesses.")
      if turns == 0:
        print("You lose!")
        choice = input("Would you like to play again? y/n\n")
        if "y" in choice:
          play()
        elif "n" in choice:
          sys.exit()
        else:
          print("Something went wrong, type y or n.")
play()
