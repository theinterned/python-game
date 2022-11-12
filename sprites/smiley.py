import arcade

# Set constants for the screen size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


def main():
    open_window()

    # Set the background color to white.
    # For a list of named colors see:
    # http://arcade.academy/arcade.color.html
    # Colors can also be specified in (red, green, blue) format and
    # (red, green, blue, alpha) format.
    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    # draw face
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

    #  draw right eye
    x = 370
    y = 370
    radius = 70
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    #  draw left eye
    x = 220
    y = 370
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    # draw smile
    x = 300
    y = 220
    width = 500
    height = 100
    start_angle = 190
    end_angle = 350
    thickness = 10
    arcade.draw_arc_outline(
        x, y, width, height, arcade.color.BLACK, start_angle, end_angle, thickness)

    arcade.finish_render()

    arcade.run()


def open_window():
    """Open window, preferring opening on second display"""
    screens = arcade.get_screens()
    screen = screens[(0, 1)[len(screens) > 1]]
    window = arcade.open_window(
        WINDOW_WIDTH, WINDOW_HEIGHT, "Smiley Face")
    winX = screen.x + screen.width // 2 - window.width // 2
    winY = screen.y + screen.height // 2 - window.height // 2
    window.set_location(winX, winY)
    return window


main()
