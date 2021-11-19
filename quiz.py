import re
import random

terms = """3 common views of a multiview drawing are Top, Front, Right side views
CAD = Computer Aided Design/Drafting
CIM = Computer Integrated Manufacturing
CNC = Computer Numeric Control
A keyboard, mouse, and touchscreen are examples of input devices.
The metric system is the most common measurement system used around the world.
Always secure your work before you drill on the drill press.
The first coat of paint is called primer.
A culvert is a tunnel for water, it is not classified as a bridge.
3d printers create three-dimensional objects by adding layers of plastic.
After creating a prototype, engineers test and evaluate to improve the design.
When drawing on AutoCad, in order to duplicate an object several times use copy command.
Environmental engineers design solar panels and windmills.
In autocad, erase command is used to remove unwanted lines.
Abrasive = sand paper.
The band saw always cuts on the down stroke direction.
The ability to make identical parts to work without getting tired and to work in dangerous situations are all advantages of a CNC machine.
All CNC Machines/Robots operate from a home position.
Robots can be used to do repetitive and dangerous jobs.
The smoothest grit of sand paper we will use in the shop/lab is 400.
The lines that are used in technical drawings are called the alphabet of lines.
Technology system is when parts work together to achieve a common goal.
When using CNC machine you must have x, y, & z axis to show direction with Cartesian.
Battery is a portable power source.
Engineerings are expected to stay up-to-date with the current technologies.
Engineers communicate with verbal, written, and CAD communication.
The first step in the Engineering design process is define the problem.
"""

def gen_quiz(terms, fix:bool=True):
    if fix:
        cards = terms.replace("=", "is")
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

gen_quiz(terms)