# Guess Letters (Hangman) https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

# write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly
# keep track of the letters the player guessed and display a different message if the player tries to guess that letter again
# stop the game when all the letters have been guessed correctly
# the player can only guess 6 letters incorrectly before losing

from random import randrange
word_list = ["Python","Java","JavaScript","PHP","R","TypeScript","Go","Swift","Cobol"]
word = word_list[randrange(len(word_list))]

print("_ " * len(word))

wrong_ans = 0
guess_list= []

def show_word():
    count = 0
    for letter in word.lower():
        if letter in guess_list:
            print(letter, end=" ")
        else:
            count += 1
            print("_", end=" ")
    print("")
    return count

while True:
    if wrong_ans > 5:
        print("You got HANGED!!")
        break
    else:
        guess = input("Please enter a letter: ").lower()
        if len(guess) > 1 or not guess.isalpha():
            print("You put in a non letter or more than one letter.  You clearly dont know games")
            continue
        elif guess in guess_list:
            print("You silly goose you already guessed that")
            continue
        elif guess in word.lower():
            guess_list.append(guess)
            if show_word() == 0
                print("You won the game!")
                break
        else:
            wrong_ans += 1
            guess_list.append(guess)
            print("You chose wrong buddy. You have {} more guesses".format(6 - wrong_ans))
        
         























