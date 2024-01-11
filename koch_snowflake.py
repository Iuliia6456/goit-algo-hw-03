import sys
import turtle
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

def get_recursion_level():
    while True:
        try:            
            recursion_level = int(input("\nEnter the level of recursion (an integer): "))
            return recursion_level
        
        except ValueError:
            print("\nPlease enter an integer")
        except KeyboardInterrupt:
            logging.info("\nProgram finished\n")
            sys.exit()
        
def main():

    recursion_level = get_recursion_level()

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-150, 0)
    my_turtle.pendown()

    for _ in range(3):
        koch_snowflake(my_turtle, recursion_level, 300)
        my_turtle.right(120)

    my_turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
