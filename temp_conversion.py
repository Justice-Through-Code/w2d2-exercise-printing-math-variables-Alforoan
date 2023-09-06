
def convert_100_to_celsius():
    f = 100
    celsius_100 = (f-32) * 5/9
    if(type (celsius_100) == float):
        print("float")
    else:
        print('integer')
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is

convert_100_to_celsius()

def convert_0_to_celsius():

    f = 0
    celsius_0 = (f-32) * 5/9
    print(celsius_0)
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value

convert_0_to_celsius()

def convert_34_2_to_celsius():
    print((34.2-32) * 5/9)
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    
convert_34_2_to_celsius()


# Now, can you convert back?


def convert_5_to_fahrenheit():
    c = 5
    f = c * 1.8 + 32

    print(f)
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out

convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    f = 85.1
    c = (f-32) * 5/9
    
    c2 = 30.2
    f2 = c2 * 1.8 + 32

    if(c > f2):
        print('85.1 degrees fahrenheit')
    elif(f2 > c):
        print('30.2 degrees celsius')

    

hotter_temp()
