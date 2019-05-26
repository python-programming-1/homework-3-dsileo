def collatz(num):
    if num % 2 == 0:
        new_variable = num / 2
    else:
        new_variable = 3 * num + 1
    print(new_variable)
    return new_variable

user_input = None
while user_input is None:
    print('Enter an integer, please.')
    user_input = input()
    
    try:
        user_input = int(user_input)
    except ValueError:
        print("That's not an integer, dude.")
        user_input = None

function_output = user_input
while function_output != 1:
    function_output = collatz(function_output)





##Print and return the num
##Catch non int w/ try and except
##Stop when 1 is returned int
##While loop for Collatz function and keep calling back
##Use Modulo divison