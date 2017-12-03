#CA5 part B - involves modifying your calculator class from CA1 to ensure that it can handle lists of data.
#You will be required to refactor / rewrite your functions so that they can handle lists.
#You will need to use lambda, map, filter, reduce and list comprehension in any manner you deem necessary to achieve this.
#Submit a Python script of your program to moodle and github as well as any tests you have done which should still work.
#The deadline is the 3rd December 2017 on moodle @ 23:55.

def welcome():
    print('''
Welcome to Andrea's Calculator
''')

welcome()


# 1. Addition
def add(a, b):
    return map(lambda x, y: x+y, a, b)	

# 2. Subtraction
def subtract(a, b):
    return map(lambda x, y: x-y, a, b)	
        
# 3. Multiplication	
def multi(a, b):
    return map(lambda x, y: x*float(y) if y!=0 else 'nan', a, b) 
        
# 4. Division	
def div(a, b):
    return map(lambda x, y: x/float(y) if y!=0 else 'nan', a, b) 

# 5. Exponential    
def expo(a, b):
    return map(lambda x, y: x**y, a, b)

# 6. Square   
def sqr(values):
    return map(lambda x: x**2,values)
        
# 7. Cube 
def cbe(values):	
    return map(lambda x: x*x*x, values)
   
# 8. Remainder
def rem(a,b):	
    return map(lambda x, y: x%y, a, b)
  
# 9. Square Root MAL
def sqrt(values):	
    return map(lambda x : x ** 0.5, values) 
    
# 10. Cube Root MAL
def cbrt(values):	
    return map(lambda x : x ** 1/3, values)   
    
#Print Results      
print 'Results'

print '1.Adition result :',add([67,3,56], [5,78,90])   
print '2.Subtraction result :',subtract([4,123,56], [4,211,45])   
print '3.Multiplication result :',multi([1, 4, 4, 8, 10], [2, 3, 6, 7, 9])
print '4.Division result :',div([0, 36, 12],[2, 7, 9])
print '5.Exponential result :',expo([3, 6, 12], [2, 3, 5])
print '6.Square result of: 2, 4, 5 =',sqr([2, 4, 5])
print '7.Cube result:',cbe([1, 4, 10])
print '8.Remainder result:',rem([12, 5, 32],[5,2,7])
print '9.Square Root :',sqr([2, 6, 9])
print '10.Cube Root result :',cbrt ([2, 6, 9])

print ' '
print 'Filter example'
print ' '
#Filtering
    
lista = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, lista)
print 'Odd  numbers on [0,1,1,2,3,5,8,13,21,34,55]',result

# here all the even numbers
result = filter(lambda x: x != 0 and x % 2 == 0, lista)
print 'Even numbers on [0,1,1,2,3,5,8,13,21,34,55]',result

print ' '
print 'Reduce example'
print ' '
#Reducing

add = reduce(lambda x,y: x+y, [47,11,42,13])
print 'Reduce add list: [47,11,42,13] result =',add
multiply = reduce(lambda x,y: x*y, [47,11,42,13])
print 'Reduce mutiply list : [47,11,42,13] result =',multiply
subtract = reduce(lambda x,y: x-y, [47,11,42,13])
print 'Reduce subtract list : [47,11,42,13] result =',subtract
