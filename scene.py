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
    """A Scene object is a Frame that uses the tkinter library
    to draw a somewhat realistic outdoor scene in the frame.
    """

    def __init__(self):
        """Initialize a Scene object."""

        # Call __init__ in the parent class.
        super().__init__()

        self.master.title("Scene")
        self.pack(fill=BOTH, expand=1)

        # Get a canvas object that will draw into this Scene object.
        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        # Call the draw_scene function.
        draw_scene(canvas, 0, 0, 799, 599)


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.

    param scene_left - left side of region; less than scene_right
    param scene_top - top of the region; less than scene_bottom
    param scene_right - right side of the region
    param scene_bottom - bottom of the region

    The width and height of the region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    canvas.create_oval(scene_left + 20, scene_top + 40,
            scene_right - 60, scene_bottom - 80,
            outline="#404040", width=4, fill="#2040e0")

    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


# Call the main function so that
# this program will start executing.
main()