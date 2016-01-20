#simple calculator to add, subtract, multiply and divide two numbers
def validate_input( prompt):
        while True:
                try:
                    valid_input=raw_input(prompt)
                    valid_input=int(valid_input)
                    return valid_input
                    break
                except ValueError:
                        print "Enter a number, please try again"
                        continue
def input_numbers():
    global a
    global b
    First_number="Enter first number: "
    a=validate_input(First_number)
    Second_number="Enter second number: "
    b=validate_input(Second_number)
    
def add():#function to prompt user for 2 numbers,add them and print result
    input_numbers()
    print "The answer is: %d + %d = %d" %(a,b,a+b)



def subtract():#function to prompt user for 2 numbers, subtract them and print result
    input_numbers()
    print "The answer is: %d - %d = %d" %(a,b,a-b)



def multiply():#function to prompt user for 2 numbers, multiply them and print result
    input_numbers()
    print "The answer is: %d * %d = %d" %(a,b,a*b)


def divide():#function to prompt user for 2 numbers, multiply them and print result
    input_numbers()
    if b==0:
            print "Invalid denominator"
            input_numbers()   
    print "The answer is: %d / %d =" %(a,b),
    print float(a)/b

def calculator():
    print "Select Operation"
    print "1.ADD"
    print "2.SUBTRACT"
    print "3.MULTIPLY"
    print "4.DIVIDE"
    choice_in="Enter choice(1/2/3/4): "#prompting user to choose an option
    choice=validate_input(choice_in)
    if choice==1:
        add()
    elif choice==2:
        subtract()
    elif choice==3:
        multiply()
    elif choice==4:
        divide()
    else:
        print "Invalid choice"
while(1):
        calculator()

    
    




        



		
