import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    t.clear()
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    koch_curve(t, order, size)

# Initialize turtle once
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter a Koch order (1–10) or 'q' to quit: ").strip()

        if user_input.lower() == "q":
            print("Exit by user command.")
            break

        try:
            user_input = int(user_input)
        except ValueError:
            print("Please enter an integer value.")
            continue

        if user_input > 10:
            print("Value too big")
            continue
        if user_input < 1:
            print("Value too small")
            continue
        draw_koch_curve(user_input)

    print("Exiting...")
    turtle.done()