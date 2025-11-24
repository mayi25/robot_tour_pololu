""" Check the steps """
try:
    STARTED = False
    direction = [0, 1]
    position = [0, 0]
    with open("main.py", 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split("#")[0].rstrip()
            if line != "first_box()" and not STARTED:
                continue
            match line:
                case "first_box()":
                    STARTED = True
                case "left()":
                    old_zero = direction[0]
                    direction[0] = -direction[1]
                    direction[1] = old_zero
                    position[0] += direction[0]
                    position[1] += direction[1]
                case "right()":
                    old_zero = direction[0]
                    direction[0] = direction[1]
                    direction[1] = -old_zero
                    position[0] += direction[0]
                    position[1] += direction[1]
                case "turn_left_bottle()" | "turn_left()":
                    old_zero = direction[0]
                    direction[0] = -direction[1]
                    direction[1] = old_zero
                case "turn_right()" | "turn_right_bottle()":
                    old_zero = direction[0]
                    direction[0] = direction[1]
                    direction[1] = -old_zero
                case "push_bottle()" | "front()":
                    position[0] += direction[0]
                    position[1] += direction[1]
                case "back()":
                    position[0] -= direction[0]
                    position[1] -= direction[1]
except FileNotFoundError:
    print("Error: The file main.py was not found.")

print(position)
print(direction)