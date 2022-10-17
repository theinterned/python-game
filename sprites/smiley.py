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
