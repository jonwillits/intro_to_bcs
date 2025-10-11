from src.display import app
import params

if __name__ == "__main__":

    the_params = params.Params()
    app = app.App(the_params)
    app.root.mainloop()