import re
import random

f = open("terms.txt", "r")
terms = f.read()
f.close()

def gen_quiz(terms, fix:bool=True):
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
            remWordIndex = random.randint(0, len(term.split(" ")) - 1)
            termList = term.split(" ")
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