from tkinter import Tk, Canvas, Frame, BOTH


def main():
    # Create the root Tk object.
    root = Tk()

    # Create a Scene window. Creating an object
    # calls the __init__ function in the class.
    Scene()

    root.geometry("800x600")
    root.mainloop()


class Scene(Frame):
    # A Scene object is a Frame that uses the tkinter library
    #to draw a somewhat realistic outdoor scene in the frame.
    

    def __init__(self):
        # Initialize a Scene object.

        # Call __init__ in the parent class.
        super().__init__()

        self.master.title("Scene")
        self.pack(fill=BOTH, expand=1)

        # Get a canvas object that will draw into this Scene object.
        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        # Draw Scene
        draw_scene(canvas, 0, 0, 800, 600)


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):

    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_clouds(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_grass(canvas, scene_left, scene_top, scene_right, scene_bottom)
# Define Sky.
def draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_rectangle(scene_left, scene_top,
             scene_right, scene_bottom - 200,
             outline="#93ffff", width=0, fill="#93ffff")
# Define Ground
def draw_ground(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_rectangle(scene_left, scene_top + 400,
             scene_right, scene_bottom,
             outline="#55311e", width=0, fill="#55311e")
# Define Clouds
def draw_clouds(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_oval(scene_left + 650, scene_top + 0,
            scene_right - 25, scene_bottom - 500,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 550, scene_top + 75,
            scene_right - 100, scene_bottom - 425,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 600, scene_top + 35,
            scene_right - 50, scene_bottom - 475,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 500, scene_top + 0,
            scene_right - 150, scene_bottom - 500,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 450, scene_top + 75,
            scene_right - 200, scene_bottom - 425,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 400, scene_top + 35,
            scene_right - 250, scene_bottom - 475,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 25, scene_top + 50,
            scene_right - 650, scene_bottom - 450,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 100, scene_top + 125,
            scene_right - 550, scene_bottom - 375,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 50, scene_top + 75,
            scene_right - 600, scene_bottom - 425,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 150, scene_top + 50,
            scene_right - 500, scene_bottom - 450,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 200, scene_top + 125,
            scene_right - 450, scene_bottom - 375,
            outline="#EDF6F6", width=2, fill="#FFFFFF")

    canvas.create_oval(scene_left + 250, scene_top + 75,
            scene_right - 400, scene_bottom - 425,
            outline="#EDF6F6", width=2, fill="#FFFFFF")
# Define Grass
def draw_grass(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_rectangle(scene_left + 0, scene_top + 350,
            scene_right - 790, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 15, scene_top + 375,
            scene_right - 775, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 30, scene_top + 350,
            scene_right - 760, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 45, scene_top + 375,
            scene_right - 745, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 60, scene_top + 350,
            scene_right - 730, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 75, scene_top + 375,
            scene_right - 715, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 90, scene_top + 350,
            scene_right - 700, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 105, scene_top + 375,
            scene_right - 685, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 120, scene_top + 350,
            scene_right - 670, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 135, scene_top + 375,
            scene_right - 655, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 150, scene_top + 350,
            scene_right - 640, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 165, scene_top + 375,
            scene_right - 625, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 180, scene_top + 350,
            scene_right - 610, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 195, scene_top + 375,
            scene_right - 595, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 210, scene_top + 350,
            scene_right - 580, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 225, scene_top + 375,
            scene_right - 565, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 240, scene_top + 350,
            scene_right - 550, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 255, scene_top + 375,
            scene_right - 535, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 270, scene_top + 350,
            scene_right - 520, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 285, scene_top + 375,
            scene_right - 505, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 300, scene_top + 350,
            scene_right - 490, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 315, scene_top + 375,
            scene_right - 475, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 330, scene_top + 350,
            scene_right - 460, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 345, scene_top + 375,
            scene_right - 445, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 360, scene_top + 350,
            scene_right - 430, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 375, scene_top + 375,
            scene_right - 415, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 390, scene_top + 350,
            scene_right - 400, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 405, scene_top + 375,
            scene_right - 385, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 420, scene_top + 350,
            scene_right - 370, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 435, scene_top + 375,
            scene_right - 355, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 450, scene_top + 350,
            scene_right - 340, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 465, scene_top + 375,
            scene_right - 325, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 480, scene_top + 350,
            scene_right - 310, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 495, scene_top + 375,
            scene_right - 295, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 510, scene_top + 350,
            scene_right - 280, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 525, scene_top + 375,
            scene_right - 265, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 540, scene_top + 350,
            scene_right - 250, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 555, scene_top + 375,
            scene_right - 235, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 570, scene_top + 350,
            scene_right - 220, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 585, scene_top + 375,
            scene_right - 205, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 600, scene_top + 350,
            scene_right - 190, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 615, scene_top + 375,
            scene_right - 175, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 630, scene_top + 350,
            scene_right - 160, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 645, scene_top + 375,
            scene_right - 145, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 660, scene_top + 350,
            scene_right - 130, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 675, scene_top + 375,
            scene_right - 115, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 690, scene_top + 350,
            scene_right - 100, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 705, scene_top + 375,
            scene_right - 85, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 720, scene_top + 350,
            scene_right - 70, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 735, scene_top + 375,
            scene_right - 55, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 750, scene_top + 350,
            scene_right - 40, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 765, scene_top + 375,
            scene_right - 25, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 780, scene_top + 350,
            scene_right - 10, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")

    canvas.create_rectangle(scene_left + 795, scene_top + 375,
            scene_right - 0, scene_bottom - 0,
            outline="darkgreen", width=1, fill="green")


# Call the main function so that
# this program will start executing.
main()