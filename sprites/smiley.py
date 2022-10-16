import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Smiley Face")

# Set the background color to white.
# For a list of named colors see:
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
arcade.set_background_color(arcade.color.WHITE)

arcade.run()
