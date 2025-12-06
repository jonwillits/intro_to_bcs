from src import ai
from src import app
from src import rock_paper_scissors

def main():
    show_ai = False
    computer_strategy = 'Smart'
    the_ai = ai.AI(computer_strategy)
    the_game = rock_paper_scissors.RockPaperScissors(the_ai)
    the_display = app.App(the_game, show_ai)
    the_display.root.mainloop()

main()
