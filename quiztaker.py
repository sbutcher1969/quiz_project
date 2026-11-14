# .qmf is the code for quizmaker files
# this is the mvp for running the bot in discord
import pickle
import sys
import glob

from rich import inspect, pretty
from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.style import Style


console = Console()

console.clear()
quizlist: list[Question] = []
quizanswers: list[str] = []
scorelist= []

class Question(object):
    def __init__(
        self,
        questnub: int,
        question: str,
        answer: list[str],
        correctans: str,
        explain: str,
    ):
        self.questnub: int = questnub
        self.question: str = question
        self.answer: list[str] = answer
        self.correctans: str = correctans
        self.explain: str = explain


class PlayerScore(object):
    def __init__(self, quizname: str, highscore:int, tenscores: list[int]
    ):
        self.quizname: str = quizname
        self.highscore:int = highscore
        self.tenscores:list[int] = tenscores


def loadquiz(quizname):
    fname = (quizname) + ".qmf"
    with open(fname, "rb") as q:
        while True:
            try:
                questnub = pickle.load(q)
                question = pickle.load(q)
                answer = pickle.load(q)
                correctans = pickle.load(q)
                explain = pickle.load(q)

                quizlist.append(
                    Question(questnub, question, answer, correctans, explain)
                )
            except EOFError:
                break

    print("Quiz Loaded!")

def loadscores(quizname,player):

    fname = (quizname) + "_" + (player) + ".qts"
    with open(fname, "rb") as q:
        while True:
            try:
                quizname = pickle.load(q)
                highscore = pickle.load(q)
                tenscores = pickle.load(q)

                scorelist.append(PlayerScore(quizname,highscore,tenscores))
            except EOFError:
                break

    print("Scores Loaded")

def takequiz(quizlist):
    quizanswers: list[str] = []
    for count, item in enumerate(quizlist, start=1):
        console.clear()
        console.print()
        console.print(Panel.fit(f"[dodger_blue1]{count}.  {item.question}  [/]"))
        print("")
        #for count, ans in enumerate(item.answer, start=1):
         #   console.print(Panel.fit(f"  [bold purple]{count}[/] {ans} "))
        x =[(x, ans) for x, ans in enumerate(item.answer,start=1)]
        console.print(Panel.fit(f"  [bold purple]{x}[/]"))
        print("")
        answered = console.input(
            "[bold green]Please input the number of the correct answer: [/]"
        )
        quizanswers.append(answered)
        print("\n\n")
    return quizanswers


def gradequiz(quizanswers: list[str]):
    grade=[]
    score: float = 0.0
    for count, x in enumerate(quizanswers, start=0):
        if quizanswers[count] == quizlist[count].correctans:
            score += 100.0 / len(quizanswers)
            grade.append("[bold green]\u2713[/]")
        else:
            grade.append("[red]X[/]")

        console.print(f"[underline]{quizanswers[count]}|[/]", end="")
    console.print("   [white]Answered[/]")
    for x in grade:
        console.print(f"{x}|",end="")
    console.print("   [green]Grade[/]")
    # print space for display of grid of right and wrong answers

    # right and wrong answers, red X and white checks. Score
    # and explanations with hover paragraphs
    # high score file needed, with a conditional it the end of everyquiz
    #     to check for high scores and record user score in his/her own
    #     dictionary in the file.

    print(" ")
    print("Final score: ",score)


def main():

    selection = input("Do you want to take a Quiz?(y/n)").lower()
    if selection == "y":
        ls = (glob.glob('*.qmf'))

        for count,a in enumerate(ls, start=1):
            b = a.split(".")
            print(f"{count}   {b[0]}")

        quizname = input("Input the name of the Quiz: ")
        loadquiz(quizname)
    elif selection == "n":
        sys.exit()
    else:
        console.print("[bold red]please select 'y' or 'n'![/]")

    selection = input("Are you ready to begin?")
    print("\n\n")
    ans = takequiz(quizlist)
    gradequiz(ans)


if __name__ == "__main__":
    main()

# TODO  
# stuff left to do ..
# finish setting up the UI
# idiot proof the user inputs
# continue towards making it into a discord
