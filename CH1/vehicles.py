import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import random, math


class HeatSource:

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


class Vehicle:

    def __init__(self, turtle_window, id_number, vehicle_type=None):
        self.speed_params = [22, 0.205, 6]
        self.turn_parameters = [20]
        self.turtle_window = turtle_window
        self.max_width = int(self.turtle_window.width / 2 - 10)
        self.max_height = int(self.turtle_window.height / 2 - 10)
        self.vehicle = RawTurtle(self.turtle_window.wn)
        self.vehicle.hideturtle()
        self.id_number = id_number

        if vehicle_type == "crossed" or vehicle_type == "direct":
            self.vehicle_type = vehicle_type
        elif vehicle_type is None:
            self.vehicle_type = random.choice(["crossed", "direct"])
        else:
            raise Exception(f"ERROR: Unrecognized vehicle type {vehicle_type}")

        self.vehicle.shape('turtle')
        self.vehicle.turtlesize(1)
        self.vehicle.penup()
        if self.vehicle_type == 'crossed':
            self.vehicle.color("red", (1, 0.85, 0.85))
        else:
            self.vehicle.color("blue", (0.85, 0.85, 1))

        self.place()
        self.vehicle.showturtle()

    def place(self):

        self.vehicle.goto(random.randint(-self.max_width, self.max_width),
                          random.randint(-self.max_height, self.max_height))
        self.vehicle.right(random.randint(0, 360))

    def __str__(self):
        output_string = f"Vehicle {self.id_number} {self.vehicle_type}"
        return output_string

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

        # Constrain x and y within the boundaries
        if x > self.max_width:
            x = self.max_width
            self.vehicle.setheading(180 - heading)  # Reflect horizontally
        elif x < -self.max_width:
            x = -self.max_width
            self.vehicle.setheading(180 - heading)  # Reflect horizontally

        if y > self.max_height:
            y = self.max_height
            self.vehicle.setheading(-heading)  # Reflect vertically
        elif y < -self.max_height:
            y = -self.max_height
            self.vehicle.setheading(-heading)  # Reflect vertically

        self.vehicle.goto(x, y)

    def compute_speed(self, left_distance, right_distance):
        if self.vehicle_type == 'crossed':
            left_speed = (self.speed_params[0] / (right_distance ** self.speed_params[1])) - self.speed_params[2]
            right_speed = (self.speed_params[0] / (left_distance ** self.speed_params[1])) - self.speed_params[2]
        else:
            left_speed = (self.speed_params[0] / (left_distance ** self.speed_params[1])) - self.speed_params[2]
            right_speed = (self.speed_params[0] / (right_distance ** self.speed_params[1])) - self.speed_params[2]
        combined_speed = (left_speed + right_speed) / 2
        return left_speed, right_speed, combined_speed


class TurtleWindow:

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

        self.simulation_id = None
        self.running = False

        self.create_window()
        self.wn.tracer(0, 0)
        self.create_heat_sources()
        self.create_vehicles()
        self.wn.update()

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

    def create_heat_sources(self):
        for i in range(self.num_heat_sources):
            self.heat_source_list.append(HeatSource(self, i))

    def create_vehicles(self):
        vehicle_count = 1
        for i in range(self.num_vehicles):
            self.vehicle_list.append(Vehicle(self, vehicle_count, vehicle_type="crossed"))
            vehicle_count += 1
        for i in range(self.num_vehicles):
            self.vehicle_list.append(Vehicle(self, vehicle_count, vehicle_type="direct"))
            vehicle_count += 1

    def reset(self):
        # Stop the simulation if it's running
        if self.running:
            self.running = False
            self.start_button.config(text="Start")

        # Clear the vehicle and heat source lists
        self.vehicle_list = []
        self.heat_source_list = []

        # Clear the screen and reset the environment
        self.wn.clear()
        self.wn.tracer(0, 0)

        # Recreate heat sources and vehicles
        self.create_heat_sources()
        self.create_vehicles()

        # Update the screen to reflect the changes
        self.wn.update()

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
        else:
            self.running = True
            self.start_button.config(text="Pause")
            self.run_simulation()

    def run_simulation(self):
        if not self.running:
            return
        for vehicle in self.vehicle_list:
            vehicle.move()
        self.wn.update()

        # Schedule the next call to run_simulation and store the ID
        self.simulation_id = self.root.after(10, self.run_simulation)

    def quit(self):
        if self.running:
            self.running = False  # Stop the simulation loop
            self.start_button.config(text="Start")

        # Cancel the scheduled run_simulation if it exists
        if hasattr(self, 'simulation_id'):
            self.root.after_cancel(self.simulation_id)

        self.root.destroy()  # Now it's safe to destroy the root


def main():
    num_turtles = 3
    num_heat_sources = 6
    screen_size = (1200,800)
    turtle_window = TurtleWindow(num_turtles, num_heat_sources, screen_size)
    turtle_window.wn.mainloop()


main()
