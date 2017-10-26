import unittest

from calculatorA import Calculator


def welcome():
    print('''
Welcome to Andrea's Calculator
''')

welcome()
        
def calculate():        
#the calculator will ask the user to select any of the options below
    operation = raw_input('''
    Please type in the math operation you would like to complete:
    +  for Addition
    -  for Subtraction
    *  for Multiplication
    /  for Division 
    ** for Exponetial
    2  for Square : 
    3  for Cube : 
    t  for Tangent : 
    s  for Sine : 
    c  for Cosine : 
    ''')

                
    if operation == '+':
        def main():
            num_1 = int(input('Enter your first number: '))
            num_2 = int(input('Enter your second number: '))
            operation = Calculator()
            print 'Result = ',operation.add(num_1,num_2)
        main ()

    elif operation == '-':
        def main():
            num_1 = int(input('Enter your first number: '))
            num_2 = int(input('Enter your second number: '))
            operation = Calculator()
            print 'Result = ',operation.subtract(num_1,num_2)
        main ()

    elif operation == '*':
        def main():
            num_1 = int(input('Enter your first number: '))
            num_2 = int(input('Enter your second number: '))
            operation = Calculator()
            print 'Result = ',operation.multiply(num_1,num_2)
        main ()
        
    elif operation == '/':
        def main():
            num_1 = int(input('Enter your first number: '))
            num_2 = int(input('Enter your second number: '))
            operation = Calculator()
            print 'Result = ',operation.divide(num_1,num_2)
        main ()
        
    elif operation == '**':
        def main():
            num_1 = int(input('Enter your first number: '))
            num_2 = int(input('Enter your exponent number: '))
            operation = Calculator()
            print 'Result = ',operation.exponent(num_1,num_2)    
        main ()
        
    elif operation == '2':
        def main():
            num_3 = int(input("Please enter a whole number: "))
            operation = Calculator()
            print 'Result = ',operation.sqr(num_3)

        main()
        
    elif operation == '3':
        def main():
            num_3 = int(input("Please enter a whole number: "))
            operation = Calculator()
            print 'Result = ',operation.cbe(num_3)

        main()   

    elif operation == 't':
        def main():
            num_3 = int(input("Please enter a whole number: "))
            operation = Calculator()
            print 'Result = ',operation.tan_calcu(num_3)

        main() 

    elif operation == 's':
        def main():
            num_3 = int(input("Please enter a whole number: "))
            operation = Calculator()
            print 'Result = ',operation.sin_calcu(num_3)

        main()

    elif operation == 'c':
        def main():
            num_3 = int(input("Please enter a whole number: "))
            operation = Calculator()
            print 'Result = ',operation.cos_calcu(num_3)

        main() 
 
    else:
        print('You have not typed a valid operator, please run the program again.')
        
    # Add again() function to calculate() function    
    again()

# Define again() function to ask user if they want to use the calculator again    
def again():
    calc_again = raw_input('Do you want to calculate again? Please type Y for YES or N for NO.')
# Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()    
    
# allow the program to be run by programs that import it.
if __name__ == '__main__':
			unittest.main()    
    
    
