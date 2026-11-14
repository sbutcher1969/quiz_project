import pickle

# from typing import List
from rich import inspect, pretty
from rich.console import Console
from rich.panel import Panel

console = Console()
console.clear()


class Quiz(object):
    def __init__(
        self, questnub: int, question: str, answer: list[str], corrans: str, explan: str
    ):
        self.questnub: int = questnub
        self.question: str = question
        self.answer: list[str] = answer
        self.corrans: str = corrans
        self.explan: str = explan

    def __str__(self):
        return f"{self.questnub},{self.question},{self.answer},{self.corrans},{self.explan}"

    def add_question(self) -> str:
        quest = input(f"Enter question number {questnub} -->")
        return quest

    def add_answer(self) -> list[str]:
        x = True
        ans_no = 0
        answ = []

        while x:
            ans_no += 1
            ans = input(f"Question {questnub}: answer number {ans_no}: ")
            if ans == "":
                x = False
            else:
                answ.append(ans)

        return answ

    def add_correct_answer(self) -> int:
        try:
            corr = input(f"What is the correct answer number? 1 - {len(answer)} : ")
        except TypeError:
            console.print("[bold red]Please select a NUMBER[/]")

        return corr

    def add_explantion(self) -> str:
        corranswer = input("Input explantion for the correct answer: ")

        if corranswer == "":
            corranswer = None

        return corranswer


# quizinst=Quiz()          # holds the instance of the Question
quizlist = []  # list to hold the quiz and Questions
loop: bool = True

while loop:
    console.print("")
    console.rule("[bold yellow]    Main Menu    [/]", style="bold green1")
    console.print("")
    console.print("[bold yellow] 1 -[/bold yellow] [green]Create Quiz[/green]")
    console.print("[bold yellow] 2 -[/] [green]View Quiz[/]")
    console.print("[bold yellow] 3 -[/] [green]Edit Quiz[/]")
    console.print("[bold yellow] 4 -[/] [green]Save Quiz[/]")
    console.print("[bold yellow] 5 -[/] [green]Load Quiz[/]")
    console.print("[bold yellow] 6 -[/] [green]Delete Quiz[/]")
    console.print("[bold yellow] 7 -[/] [green]Exit[/]")
    console.print("[yellow]")

    try:
        selection = int(
            console.input("[green] Enter your selection:[/][yellow bold] (1-7)-->")
        )
    except TypeError:
        console.print("")
        console.print(
            "[reverse red]Please input a number that corresponds with your choice![/]"
        )
        console.print("")

    if selection == 7:
        break

    if selection == 1:
        name = str(input("Enter the name:"))
        x = True
        questnub = 1
        while x:
            quest = Quiz.add_question(questnub)
            if quest == "":
                break
            answer = Quiz.add_answer(questnub)
            corran = Quiz.add_correct_answer(questnub)
            explan = Quiz.add_explantion(questnub)
            quizlist.append(Quiz(questnub, quest, answer, corran, explan))
            questnub += 1

    if selection == 2:
        for x in range(0, len(quizlist)):
            console.print(quizlist[x])
    if selection == 3:
        print("")
        print("QUESTIONS")
        print("   qa - Add question.")
        print("   qd - Delete question")
        print("ANSWERS")
        print("   aa - Add answer.")
        print("   ad - Delete answer.")
        print("EXPLANATIONS")
        print("   ea - Add explanation.")
        print("   ed - Delete explanation")
        print("")
        print("   cc - Change correct answer number.")
        print("")

        selection = input("Enter your selection to edit =>:")

        if selection == "qa":  # SELECTION  "qa"
            questnub += 1
            quest = Quiz.add_question(questnub)
            if quest == "":
                break
            answer = Quiz.add_answer(questnub)
            correctan = Quiz.add_correct_answer(questnub)
            explan = Quiz.add_explantion(questnub)
            quizlist.append(Quiz(questnub + 1, quest, answer, correctan, explan))

        if selection == "qd":  # SELECTION  "qd""
            numb = input("\n Which question to delete? =>")
            quizlist.pop(int(numb) - 1)
            for x in range(
                (int(numb)) - 1, len(quiz), 1
            ):  # Re arranging the list to be sequental
                quizlist[x].questnub = quizlist[x].questnub - 1

        if selection == "aa":  # SELECTION  "aa"
            questno = int(input("Add answer to which question? -->"))
            addanswer = Quiz.add_answer(questno)
            quizlist[questno - 1].answer.extend(addanswer)

        if selection == "ad":  # SELECTION  "ad"
            questno = int(input("Delete answer from which question? >"))
            for x in range(0, len(quizlist[questno - 1].answer)):
                print(x + 1, "    ", quizlist[questno - 1].answer[x])
            answerno = int(input("Delete which answer ?"))
            quizlist[questno - 1].answer.pop(answerno - 1)

        if selection == "ea":  # SELECTION  "ea"
            questno = int(input("Add/replace explanation for which answer? "))
            newexplan = input("Enter the new explanation -->")
            quizlist[questno - 1].explan = newexplan

        if selection == "ed":  # SELECTION  "ed"
            questno = int(input("Delete explanation for which question? "))
            quizlist[questno - 1].explan = ""

        if selection == "cc":  # SELECTION  "cc"
            questno = int(input("Change correct answer for which question? "))
            newcorrans = input(
                f"What is the correct answer number? 1 - {len(answer)} : "
            )
            quizlist[questno - 1].corrans = newcorrans

    if selection == 4:
        fname = (name) + ".qmf"
        with open(fname, "wb") as q:
            for x in range(0, len(quizlist), 1):
                pickle.dump(x + 1, q)
                pickle.dump(quizlist[x].question, q)
                pickle.dump(quizlist[x].answer, q)
                pickle.dump(quizlist[x].corrans, q)
                pickle.dump(quizlist[x].explan, q)
        print("file Saved!")

    if selection == 5:
        console.print("")
        name = console.input("What is the name of the quiz to download? -->")
        fname = (name) + ".qmf"
        with open(fname, "rb") as q:
            quizlist = []
            while True:
                try:
                    questnub = pickle.load(q)
                    question = pickle.load(q)
                    answer = pickle.load(q)
                    corrans = pickle.load(q)
                    explan = pickle.load(q)

                    quizlist.append(Quiz(questnub, question, answer, corrans, explan))
                except EOFError:
                    break

        print("file Loaded!")

    if selection == 6:
        quizlist[:] = []
        print("file Deleted!")
