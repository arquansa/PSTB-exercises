#Week1-Day 2 - Daily Challenge
#Dictionnary

word = input("Enter a word: ")
Dict = {}
index = 0

for letter in word:
    if letter.isalpha():  # checks the letter is alphabetical
        if letter not in Dict:
            Dict[letter] = [index]
        else:
            Dict[letter].append(index)
            index += 1

print(Dict)