import random

class Game:
  def __init__(self,start=1,end=100):
    self.number = random.randint(start,end)
    self.attempts = 0
    self.start = start
    self.end = end


  def play(self):
      print(f"Guess a number between {self.start} and {self.end}")
      while True:
        guess = int(input("Your guess: "))
        self.attempts += 1

        if guess==self.number:
          print(f"Congratulations! You've guessed the number {self.number} in {self.attempts} attempts.")
          break
        elif guess < self.number:
          print("Too low! Try again.")
        else:
          print("Too high! Try again.")

game =Game(1,100)
print("Secret number is:", game.number)

game.play()