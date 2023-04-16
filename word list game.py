import random
import time

time.sleep(1)
print('Really fun game, I swear')
time.sleep(2)

words = ['dust', 'legal', 'elite', 'rake']

print('Here is a pool of words: ', words)
time.sleep(3)

target = random.sample(words, 3)
print('Make it look like this list: ', target)
time.sleep(2)

def game():
    copy = words.copy()
    count = 0

    while target != copy:
        count += 1
        time.sleep(1)
        if count > 1:
            print("Here is the current list of words: ", copy)
            print("Reminder, here's the target:       ", target)
        
        print("Please choose one of the following options (by entering the number associated with the command):")
        print("1 -> Add a word to the end of the list")
        print("2 -> Add a list of words to the end of the list")
        print("3 -> Add two words in the list together (silly choice tbh)")
        print("4 -> Show the current state of the working list")
        print("5 -> Change a word in the list")
        print("6 -> Insert a word at a specific index position")
        print("7 -> Remove a word from the selected index position")
        print("8 -> Remove a selected word")
        print("9 -> Sort the list")
        print("0 -> Reset the list to its original state")
        print("86 -> Quit the game because you can't handle how fun it is")
        choice = int(input("Please make a selection: "))
                     
        if choice == 1:
            add_word = input("Please type in a word to add to the list: ")
            copy.append(add_word)
        elif choice == 2:    
            word_list = input("We will add a list of words to the end of the list.  Please enter words separated by commas: ")
            copy.extend(word_list.split(","))
        elif choice == 3:    
            word1 = input("Please enter the first word: ")
            word2 = input("Please enter the second word: ")
            copy[copy.index(word1)] += word2
            copy.remove(word2)
        elif choice == 4:    
            for word in copy:
                print(word)
        elif choice == 5:    
            old_word = input("Please type in a word from the list you wish to change: ")
            new_word = input("Please type in word you wish to replace it with: ")
            old_word_pos = copy.index(old_word)
            copy.remove(old_word)
            copy.insert(old_word_pos, new_word)
        elif choice == 6:    
            insert_word = input("Please type in a word you wish to add: ")
            insert_word_pos = int(input("Please enter the index position where this word should go: "))
            copy.insert(insert_word_pos, insert_word)
        elif choice == 7:    
            remove_word_pos = int(input("Please enter the index position of the word you wish to remove: "))
            copy.remove(copy[remove_word_pos])
        elif choice == 8:    
            remove_word = input("Please type in a word you wish to remove: ")
            copy.remove(remove_word)
        elif choice == 9:    
            order = input("How would you like to sort the list (A for ascending or D for descending): ")
            if order.lower() == 'a':
                copy.sort()
            elif order.lower() == 'd':
                copy.sort(reverse = True)
            else:    
                print("You silly goose, you entered the wrong input.")
        elif choice == 0:    
            copy = words
        elif choice == 86:
            print("You had too much fun.  Come back another time.")
            break

    print("Congrats, you beat the game!  You're the only person in the whole world that has beaten the game in the past 5 minutes.")
        
        
game()
    

