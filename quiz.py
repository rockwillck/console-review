import re
import random

f = open("terms.txt", "r")
terms = f.read()
f.close()

f = open("1-1000.txt", "r")
oneonethousand = f.read().split("\n")
f.close()

i = 0
for word in oneonethousand:
    oneonethousand[i] = word.lower()
    i += 1

def gen_quiz(terms, fix:bool=True, includeSimple:bool=False):
    cont = True
    while cont:
        if fix:
            cards = terms.replace("=", "is").replace("&", "and")
        else:
            cards = terms
        cards = cards.splitlines(False)
        random.shuffle(cards)
        while len(cards) > 0:
            term = cards[0]
            termList = term.split(" ")
            if not includeSimple:
                i = 0
                while i < 100:
                    x = True
                    remWordIndex = random.randint(0, len(term.split(" ")) - 1)
                    for word in oneonethousand:
                        if (word in termList[remWordIndex].lower()) or (termList[remWordIndex].lower() in word):
                            x = False
                    if x == True:
                        break
                    i += 1
            else:
                remWordIndex = random.randint(0, len(term.split(" ")) - 1)
            remWord = termList[remWordIndex]
            termList[remWordIndex] = "_____"
            termInputStr = ""
            for el in termList:
                termInputStr += el + " "
            termInputStr = termInputStr[:-1]
            answer = input(termInputStr + ": ")
            if fix:
                truAnswer = re.sub(r'[^a-zA-Z0-9 ]', '', answer)
            else:
                truAnswer = answer
            if fix:
                truRem = re.sub(r'[^a-zA-Z0-9 ]', '', remWord)
            else:
                truRem = remWord
            if truAnswer.lower() == truRem.lower():
                print("Correct")
                cards.remove(term)
            else:
                print(f"Incorrect: Correct answer is \"{remWord}\"")
                cards.remove(term)
                cards.append(term)
            print(str(len(cards)) + " terms remaining.")
        contInput = input("Play another round? ").lower()
        cont = False if contInput != "y" and contInput != "yes" else True

gen_quiz(terms)
