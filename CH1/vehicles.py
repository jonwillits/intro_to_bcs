import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import random, math, time


###################################################################################################################
###################################################################################################################
class HeatSource:
    ###############################################################################################################
    def __init__(self, turtle_window, id_number):
        self.turtle_window = turtle_window
        self.id_number = id_number
        self.heat_source = RawTurtle(self.turtle_window.wn)
        self.heat_source.hideturtle()
        self.heat_source.shape('circle')
        self.heat_source.penup()
        self.heat_source.color("orange")
        self.place()
        self.heat_source.showturtle()

        self.heat_source.ondrag(self.drag_heat_source)

    def place(self):
        max_width = int(self.turtle_window.width / 2 - 10)
        max_height = int(self.turtle_window.height / 2 - 10)
        self.heat_source.goto(random.randint(-max_width, max_width), random.randint(-max_height, max_height))

    def drag_heat_source(self, x, y):
        self.heat_source.goto(x, y)
        self.turtle_window.wn.update()


###################################################################################################################
###################################################################################################################
class Vehicle:
    ###############################################################################################################
    def __init__(self, turtle_window, id_number):
        self.speed_params = [20, 0.2, 6]
        self.turn_parameters = [20]
        self.turtle_window = turtle_window
        self.max_width = int(self.turtle_window.width / 2 - 10)
        self.max_height = int(self.turtle_window.height / 2 - 10)
        self.vehicle = RawTurtle(self.turtle_window.wn)
        self.vehicle.hideturtle()
        self.id_number = id_number
        self.type = random.choice(["crossed", "direct"])
        self.vehicle.shape('turtle')
        self.vehicle.turtlesize(1)
        self.vehicle.penup()
        if self.type == 'crossed':
            self.vehicle.color("red", (1, 0.85, 0.85))
        else:
            self.vehicle.color("blue", (0.85, 0.85, 1))

        self.place()
        self.vehicle.showturtle()

    def place(self):

        self.vehicle.goto(random.randint(-self.max_width, self.max_width),
                          random.randint(-self.max_height, self.max_height))
        self.vehicle.right(random.randint(0, 360))

    ###############################################################################################################
    def move(self):
        cumulative_speed = 0
        cumulative_turn_amount = 0
        for heat_source in self.turtle_window.heat_source_list:
            input_distance = self.vehicle.distance(heat_source.heat_source.pos())
            input_angle = self.vehicle.heading() - self.vehicle.towards(heat_source.heat_source.pos())
            sin_angle = math.sin(math.radians(input_angle))
            left_sensor_distance = input_distance - sin_angle
            right_sensor_distance = input_distance + sin_angle
            left_speed, right_speed, combined_speed = self.compute_speed(left_sensor_distance, right_sensor_distance)
            turn_amount = self.turn_parameters[0] * (right_speed - left_speed)
            cumulative_speed += combined_speed
            cumulative_turn_amount += turn_amount

        if isinstance(cumulative_turn_amount, complex):
            cumulative_turn_amount = 0

        if cumulative_speed < 0:
            cumulative_speed = 0

        self.vehicle.right(cumulative_turn_amount)
        self.vehicle.forward(cumulative_speed)
        self.check_border_collision()

    def check_border_collision(self):
        x, y = self.vehicle.xcor(), self.vehicle.ycor()
        heading = self.vehicle.heading()

        if x > self.max_width:
            x = self.max_width
        elif x < -self.max_width:
            x = -self.max_width

        if y > self.max_height:
            y = self.max_height
        elif y < -self.max_height:
            y = -self.max_height

        self.vehicle.goto(x, y)

        if y in [-self.max_height, self.max_height]:
            if 0 <= heading <= 180:
                turn_angle = 360 - heading
            else:
                turn_angle = heading
            self.vehicle.setheading(turn_angle)

        if x in [-self.max_width, self.max_width]:
            if heading <= 90 or heading > 270:
                turn_angle = 180 - heading
            else:
                turn_angle = heading
            self.vehicle.setheading(turn_angle)

    ###############################################################################################################
    def compute_speed(self, left_distance, right_distance):
        if self.type == 'crossed':
            left_speed = (self.speed_params[0] / (right_distance ** self.speed_params[1])) - self.speed_params[2]
            right_speed = (self.speed_params[0] / (left_distance ** self.speed_params[1])) - self.speed_params[2]
        else:
            left_speed = (self.speed_params[0] / (left_distance ** self.speed_params[1])) - self.speed_params[2]
            right_speed = (self.speed_params[0] / (right_distance ** self.speed_params[1])) - self.speed_params[2]
        combined_speed = (left_speed + right_speed) / 2
        return left_speed, right_speed, combined_speed


###################################################################################################################
###################################################################################################################
class TurtleWindow:
    ###############################################################################################################
    def __init__(self, num_vehicles, num_heat_sources, screen_size):
        self.root = None
        self.canvas = None
        self.wn = None
        self.button_frame = None
        self.start_button = None
        self.stop_button = None
        self.reset_button = None
        self.quit_button = None

        self.width = screen_size[0]
        self.height = screen_size[1]

        self.num_heat_sources = num_heat_sources
        self.heat_source_list = []

        self.num_vehicles = num_vehicles
        self.vehicle_list = []

        self.running = False

        self.create_window()
        self.wn.tracer(0, 0)
        self.create_heat_sources()
        self.create_vehicles()
        self.wn.update()

    ###############################################################################################################
    def create_window(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.wn = TurtleScreen(self.canvas)
        self.root.title("Braitenberg's Vehicle #2")
        self.wn.onkey(self.start_stop, "space")
        self.wn.listen()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Start", fg="black", command=self.start_stop)
        self.reset_button = tk.Button(self.button_frame, text="Reset", fg="black", command=self.reset)
        self.quit_button = tk.Button(self.button_frame, text="Quit", fg="black", command=self.quit)
        self.start_button.pack(side=tk.LEFT)
        self.reset_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

    ###############################################################################################################
    def create_heat_sources(self):
        for i in range(self.num_heat_sources):
            self.heat_source_list.append(HeatSource(self, i))

    ###############################################################################################################
    def create_vehicles(self):
        for i in range(self.num_vehicles):
            self.vehicle_list.append(Vehicle(self, i))

    ###############################################################################################################
    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_button.config(text="Pause")

        while self.running:
            for i in range(self.num_vehicles):
                self.vehicle_list[i].move()
            self.wn.update()
            time.sleep(0.01)

    ###############################################################################################################
    def reset(self):
        self.vehicle_list = []
        self.heat_source_list = []

        self.wn.clear()
        self.wn.tracer(0, 0)
        self.create_heat_sources()
        self.create_vehicles()
        self.wn.update()

    ###############################################################################################################
    def quit(self):
        if self.running:
            self.start_stop()
        self.root.destroy()


###################################################################################################################
###################################################################################################################
###################################################################################################################
###################################################################################################################

def main():
    num_turtles = 3
    num_heat_sources = 3
    screen_size = (1200,800)
    turtle_window = TurtleWindow(num_turtles, num_heat_sources, screen_size)
    turtle_window.wn.mainloop()


main()
