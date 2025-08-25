from src import exp
from src import app
import config

def main():
    the_app = app.App(config.Config)
    the_experiment = exp.Exp(the_app, config.Config)
    the_app.root.mainloop()

if __name__ == '__main__':
    main()