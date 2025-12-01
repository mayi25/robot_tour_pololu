""" Check the steps """
import sys

def show_pos():
    """Show  the position"""
    if VERBOSE:
        print("pos: " + str(position) + ", dir:"+ str(direction))

VERBOSE = False
if len(sys.argv) >= 2 and sys.argv[1] == "-v":
    VERBOSE = True

if len(sys.argv) >= 3 and sys.argv[2] == "-v":
    VERBOSE = True

if len(sys.argv) >= 2 and sys.argv[1] == "-l":
    MAIN_FILE = "/media/mayi/MicroPython/main.py"
else:
    MAIN_FILE = "D:\\main.py"

try:
    STARTED = False
    direction = [0, 1]
    position = [0, 0]
    total_step = 0 # pylint: disable=invalid-name
    with open(MAIN_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split("#")[0].rstrip()
            if line != "first_box()" and not STARTED:
                continue
            match line:
                case "first_box()":
                    STARTED = True
                    total_step += 1
                    show_pos()
                case "left()":
                    OLD_ZERO = direction[0]
                    direction[0] = -direction[1]
                    direction[1] = OLD_ZERO
                    position[0] += direction[0]
                    position[1] += direction[1]
                    total_step += 1
                    show_pos()
                case "right()":
                    OLD_ZERO = direction[0]
                    direction[0] = direction[1]
                    direction[1] = -OLD_ZERO
                    position[0] += direction[0]
                    position[1] += direction[1]
                    total_step += 1
                    show_pos()
                case "turn_left()":
                    OLD_ZERO = direction[0]
                    direction[0] = -direction[1]
                    direction[1] = OLD_ZERO
                    show_pos()
                case "turn_right()":
                    OLD_ZERO = direction[0]
                    direction[0] = direction[1]
                    direction[1] = -OLD_ZERO
                    show_pos()
                case "push_bottle()" | "front()" | "front_wall()":
                    position[0] += direction[0]
                    position[1] += direction[1]
                    total_step += 1
                    show_pos()
                case "back()":
                    position[0] -= direction[0]
                    position[1] -= direction[1]
                    total_step += 1
                    show_pos()
                case "cross_bottle_right()" | "cross_bottle_left()":
                    position[0] += direction[0]
                    position[1] += direction[1]
                    direction[0] = -direction[0]
                    direction[1] = -direction[1]
                    total_step += 1
                    show_pos()
except FileNotFoundError:
    print("Error: The file main.py was not found.")

print("pos: " + str(position) + ", dir:"+ str(direction))
print("total_step: " + str(total_step))
