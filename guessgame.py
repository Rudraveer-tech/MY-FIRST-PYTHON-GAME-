import random

def start_game():
    print("====================================")
    print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯")
    print("====================================")
    print("I am thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("\nEnter your guess: ")
        
        if not guess.isdigit():
            print("❌ Please enter a valid number!")
            continue
            
        guess = int(guess)
        attempts += 1 
        
        if guess < secret_number:
            print("📈 Too low! Try a higher number.")
        elif guess > secret_number:
            print("📉 Too high! Try a lower number.")
        else:
            print(f"\n🎉 CONGRATULATIONS! You guessed it in {attempts} attempts!")
            break 

start_game()
