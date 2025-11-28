""" Check the steps """
import sys

def show_pos():
    """Show  the position"""
    if VERBOSE:
        print("pos: " + str(position) + ", dir:"+ str(direction))

VERBOSE = False
if sys.argv[1] == "-v":
    VERBOSE = True

if sys.argv[1] == "-l":
    MAIN_FILE = "main.py"
else:
    MAIN_FILE = "main.py"

try:
    STARTED = False
    direction = [0, 1]
    position = [0, 0]
    with open(MAIN_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split("#")[0].rstrip()
            if line != "first_box()" and not STARTED:
                continue
            match line:
                case "first_box()":
                    STARTED = True
                    show_pos()
                case "left()":
                    OLD_ZERO = direction[0]
                    direction[0] = -direction[1]
                    direction[1] = OLD_ZERO
                    position[0] += direction[0]
                    position[1] += direction[1]
                    show_pos()
                case "right()":
                    OLD_ZERO = direction[0]
                    direction[0] = direction[1]
                    direction[1] = -OLD_ZERO
                    position[0] += direction[0]
                    position[1] += direction[1]
                    show_pos()
                case "turn_left_bottle()" | "turn_left()":
                    OLD_ZERO = direction[0]
                    direction[0] = -direction[1]
                    direction[1] = OLD_ZERO
                    show_pos()
                case "turn_right()" | "turn_right_bottle()":
                    OLD_ZERO = direction[0]
                    direction[0] = direction[1]
                    direction[1] = -OLD_ZERO
                    show_pos()
                case "push_bottle()" | "front()":
                    position[0] += direction[0]
                    position[1] += direction[1]
                    show_pos()
                case "back()":
                    position[0] -= direction[0]
                    position[1] -= direction[1]
                    show_pos()
                case "cross_bottle()":
                    position[0] += direction[0]
                    position[1] += direction[1]
                    direction[0] = -direction[0]
                    direction[1] = -direction[1]
                    show_pos()
except FileNotFoundError:
    print("Error: The file main.py was not found.")

print("pos: " + str(position) + ", dir:"+ str(direction))
