# Simple String Concatenation and Evaluation

def Main():

#print start of program

    print("This program will show the result from mixing primary colors. Follow each instruction and hit enter.")
   
#set variables as results of modules
   
    first_color = str(color1())
    second_color = str(color2(first_color))
    result_color = mixing(first_color,second_color)

# print color mixing results
    print('The resulting color is ' + str(result_color) + '.')

# define module for getting color 1. Returns color 1

def color1():
    color = str(input('Choose the first color. Type "red", "yellow", or "blue": ')).lower()
    if color not in ('red', 'yellow', 'blue'):
         print('Your entry was not a listed color')
         color1()
    else:
        return color

# define module for getting color 2. Include result of color1 for duplicate check. Returns color 2

def color2(x):
    color = str(input('Choose a different selection for the second color. Type "red", "yellow", or "blue": ')).lower()
    if color not in ('red', 'yellow', 'blue'):
         print('Your entry was not a listed color')
         color2(x)
    elif color == str(x):
         print('You picked the same color twice.')
         color2(x) 
    else:    
        return color

# define module for getting mixed color result. Return result

def mixing(j, k):

    if 'blue' in j+k and 'red' in j+k:
        color3 = 'purple'
    elif 'yellow' in j+k and 'red' in j+k:
        color3 = 'orange'
    elif 'blue' in j+k and 'yellow' in j+k:
        color3 = 'green'
    return color3

Main()