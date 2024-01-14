import random

print("HANGMAN")
name=input("Enter name:")
print("Welcome",name,",lets play Hangman")
print("Guess the characters of the blanks to find the word")


#code for the game
list1=['Computer','Science','Hello','House','Elephant','Sunshine','Guitar','Pizza','Butterfly','Chocolate','Rainbow','Baseball','Watermelon','Fireworks']
word=random.choice(list1).lower()
print(word)
guess=6
print("_"*len(word))
wordlist=list(word)
#print(wordlist)
guesslist=list('_'*len(word))
#print(guesslist)
while guess > 0:
    found = False
    for i in range(len(wordlist)):
        char = input("Guess a character: ")
        char = char.lower()

        if char in wordlist:
            for j in range(len(wordlist)):
                if wordlist[j] == char:
                    guesslist[j] = char
                    found = True

            for k in guesslist:
                print(k, end="")
            print("\nGuesses remaining:", guess)
        else:
            if guess == 1 :
                print("Wrong guess")
                print("Out of guesses! The word was:", word)
                guess = 0
                found = True
                break
            guess = guess - 1
            print("Wrong guess")
            print("Guesses remaining:", guess)

        if guesslist == wordlist:
            print("Congratulations! You guessed the word:", ''.join(guesslist))
            found = True
            break

    if found:
        break
