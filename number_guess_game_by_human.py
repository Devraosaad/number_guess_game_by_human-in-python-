import random 

print("Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100. Try to guess it!")
number_to_guess = random.randint(1, 100)
number_of_guesses = 0
guessed_correctly = False
while True:
 while not guessed_correctly:
  num1 = int((input("Enter the Number :")))
  number_of_guesses += 1
 #if num1 == number_to_guess:
  #print("you have won the game")
 
  if num1 > number_to_guess:
        
        print("Too high! Try again.")

  elif num1 < number_to_guess:
        print("Too low! Try again.")

  else:
       guessed_correctly = True
       print(f"Congratulations! You guessed the number in {number_of_guesses} attempts.")        
 next_calculation = input("Let's do play the game ? (yes/no): ")
 if next_calculation.lower() != 'yes':
        break




    