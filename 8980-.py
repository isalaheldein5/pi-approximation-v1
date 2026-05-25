

def findLetter(word, letter, hidden):
    newHidden = ""
    for i in range(len(word)):
        if word[i] == letter:
            newHidden = newHidden + letter
        else:
            newHidden = newHidden + hidden[i]
    return newHidden


word = input("Enter the word: ")

# create hidden version
hidden = ""
for i in range(len(word)):
    hidden += "*"

won = False

for attempt in range(8):
    letter = input("Enter a letter: ")
    hidden = findLetter(word, letter, hidden)
    print(hidden)

    # check if player has won
    if "*" not in hidden:
        won = True
        print("You won!")
        break

# if loop ends and not won
if not won:
    print("You lost! The word was:", word)
