""""
ERROR DEBUGGING:
The following are totally acceptable in python:
passing a string representation of an integer into int
passing a string representation of a float into float
passing a string representation of an integer into float
passing a float into int
passing an integer into float
But you get a ValueError if you pass a string representation of a float into int,
or a string representation of anything but an integer (including empty string).
If you do want to pass a string representation of a float to an int,
as mentioned earlier above, you can convert to a float first, then to an integer:
"""

name = input("What is your name? ")
my_number = 0

# Loop as long as "my_number" is less than 100
while(my_number < 100):
    # Ask users for a number
    my_number = input("Hello "+name+" please pick a number that's bigger than 100: ")
    # Convert users' answer from a string to an integer
    my_number = int(my_number)
    print("Your number is "+ str(float(my_number)))
    # Check if the number is bigger than 100
    if(my_number > 100):
        print("That's a big number!")
    elif(my_number > 90):
        print("Almost there! Try again!")
    else:
        print("That number is too small! Please try again!")
    # If my_number is smaller than 100 at this point, loop again