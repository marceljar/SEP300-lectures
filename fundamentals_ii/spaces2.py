# Bad: no spaces around operators
x=5
y=10
result=(x+y)*(x-y)

# Bad: extra spaces inside brackets/parentheses/braces
numbers = [1 ,2 ,3 , 4,5 ]
point = ( 3,4 )
person = { "name" : "Alice" , "age" :30 }

# Bad: spaces around '=' in keyword/default arguments
def greet(name, msg = "Hello" ):
    print(f"{msg}, {name}!" )

# Bad: missing blank lines between class/functions
class Calculator:
    def add(self,a,b): return a+b
    def subtract(self,a,b):return a-b
def square(n):return n*n

# Bad: trailing spaces at line end
if x>0:    
    print("Positive number")     
