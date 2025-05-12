import turtle
import math

def pythagoras_tree(t, length, order):
    if order == 0:
        return

    # Малюємо основну гілку
    t.forward(length)

    # Зберігаємо поточну позицію і кут
    pos = t.pos()
    angle = t.heading()

    # Малюємо праву гілку
    t.left(45)
    pythagoras_tree(t, length * math.sqrt(2) / 2, order - 1)

    # Повертаємося до попереднього положення та кута
    t.setpos(pos)
    t.setheading(angle)

    # Малюємо ліву гілку
    t.right(45)
    pythagoras_tree(t, length * math.sqrt(2) / 2, order - 1)

    # Повертаємося до початку цієї гілки
    t.setpos(pos)
    t.setheading(angle)
    t.backward(length)

def draw_pythagoras_tree(order, length=80):
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)  # Повернутися вгору
    t.pendown()
    pythagoras_tree(t, length, order)

# Ініціалізація
window = turtle.Screen()
window.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(1)

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter an order (1–10) or 'q' to quit: ").strip()

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

        draw_pythagoras_tree(user_input)

    print("Exiting...")
    turtle.done()
