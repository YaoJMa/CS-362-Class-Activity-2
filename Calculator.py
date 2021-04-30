#calc Program
def add(num1, num2):
	return num1+num2

def sub(num1, num2):
	return num1-num2

def div(num1, num2):
	return num1/num2

def mult(num1, num2):
	return num1*num2

print("Select an operation: ")
print("1. Add")
print("2. Subtract")
print("3. Divide")
print("4. Multiply")

select = int(input("Select operation: "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if select == 1:
    print(number1, "+", number2, "=",
                    add(number1, number2))
  
elif select == 2:
    print(number1, "-", number2, "=",
                    sub(number1, number2))
  
elif select == 3:
    print(number1, "/", number2, "=",
                    div(number1, number2))
  
elif select == 4:
    print(number1, "*", number2, "=",
                    mult(number1, number2))
else:
    print("Invalid input")
