#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
from Words import word_list


# In[15]:


def get_valid_word(words):
    word = random.choice(word_list)
    while '-' in word or '' in word:
        word = random.choice(word_list)
    return word.upper()


# In[17]:


def hangman(word):
    word_need = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    lives = 6
    
    print("Let's start the game")
    print("\n You have" + lives + "lives, Start guessing")
    print(word_need)
    
    while not guesssed and lives>0:
        
        guess = input("Please guess a letter or a word").upper()
        
        #If you are guessing a letter
        
        if len(guess) == 1  and guess.isalpha(): 
            
            if guess in guessed_letters:                #If you have already guessed a letter
                print("You have already guessed this letter", guess)
                
            elif guess not in word:                     #If your guess is wrong
                print("Wrong guess")
                lives -= 1
                guessed_letters.append(guess)
                
            else:                                       #If your guess is right
                print("You guessed a right letter")
                guessed_letters.append(guess)
                word_as_list = list(word_need)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_need = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        
        #If you are guessing a word
        
        elif len(guess) == len(word) and guess.isalpha():
            
            if guess in guessed_words:                #If you have already guessed this word
                print("You have already guessed this word", guess)
                
            elif guess not in word:                     #If your guess is wrong
                print("Wrong guess")
                lives -= 1
                guessed_words.append(guess)
            
            else:
                print("You guessed the right word")
                guessed = True 
                word_need = word
        
        #If not a valid guess
        
        else:
            
            print("Not a valid guess.")
            print(word_need)
            print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


# In[ ]:


def main():
    word = get_valid_word(words)
    hangman(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_valid_word()
        hangman(word)


if __name__ == "__main__":
    main()

