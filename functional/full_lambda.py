from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
            
result = reduce(lambda num1, num2 : num1 + num2, \
         map(lambda num : num ** 2, \
         filter(lambda num : num % 2 == 0, numbers)))

print("The sum of even squares is:", result)
