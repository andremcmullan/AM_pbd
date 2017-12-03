# CA5 - Andrea Guzman McMullan - 10362060
#
# Part A -  designed calculator program from CA1 to test R skills, .
# set of 10 functions in R.

#1
add <- function(x, y) {
  return(x + y)
}

#2
subtract <- function(x, y) {
  return(x - y)
}

#3
multiply <- function(x, y) {
  return(x * y)
}

#4
divide <- function(x, y) {
  return(x / y)
}

#5
exponent <- function (X, y) {
  return(x^y)
}

#6
square <- function (x){
  x^2
}
#7
cube <- function(x){
  return(x ** 3)
}


#8
remainder <- function(x, y){
  return(x %% y)
}

#9
Factorial <- function(x){
  if (x == 0){
    return (1)
  }
  if (x < 0){
    return (NaN)
  }
  else{
    return (x * factorial(x - 1))
  }
}

#10
SumSquares <- function (x, y){
  return ((x ^ 2) + (y ^ 2))
}

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Square")
print("7.Cube")
print("8.Remainder")
print("9.Factorial")
print("10.SumSquare")

choice <- as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9/10]: "))

    num1 = as.integer(readline(prompt="Enter first number: "))
    num2 = as.integer(readline(prompt="Enter second number: "))
  

operator <- switch(choice,"+","-","*","/","^","^2","^3","%%","!","+^2")
result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), 
                 divide(num1, num2), exponent(num1, num2), square(num1), cube(num1), 
                 remainder(num1, num2), factorial(num1), SumSquares(num1, num2))

print(paste(num1, operator, num2, "=", result))

