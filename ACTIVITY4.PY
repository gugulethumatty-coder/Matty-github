Import random
secret=random.rand(0,10)
for i in range(3):
    guess=int(input("Guess a number between 0 and 10: "))
    if guess==secret:
        print("Numbers match! You win!")
        break
    else guess>secret:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
        print("the secret number was {secret}. Better luck next time!")