

class Calculator(object):
# Addition
    def add(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError
 # Subtraction
    def subtract(self, x, y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
# Multiplication
    def multiply(self, x,y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x*y
        else:
            raise ValueError
# Division
    def divide(self, x,y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return float(x/y)
        else:
            raise ValueError            
#The exponent of a number says how many times to use that number in a multiplication
    def exponent(self, x,y):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x**y
        else:
            raise ValueError            
#a square is the result of multiplying a number by itself
    def sqr(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return x**2
        else:
            raise ValueError            
#cube is a number multiplied by itself three times
    def cbe(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            return x**3
        else:
            raise ValueError

#The tangent of the angle = the length of the opposite side. the length of the adjacent side.           
    def tan_calcu(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            import math
            return math.tan(x)
        else:
            raise ValueError   
            
#The sine of the angle = the length of the opposite side. the length of the hypotenuse.
    def sin_calcu(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            import math
            return math.sin(x)
        else:
            raise ValueError   
            
#The cosine of the angle = the length of the adjacent side. the length of the hypotenuse.                        
    def cos_calcu(self, x):
        number_types = (int, long, float, complex)
 
        if isinstance(x, number_types):
            import math
            return math.cos(x)
        else:
            raise ValueError
        



