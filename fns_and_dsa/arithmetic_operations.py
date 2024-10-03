def perform_operation(num1,num2,operation):
  if operation == 'add':
    result = num1 + num2
  elif operation == 'subtract':
    result = num1 - num2
  elif operation == 'multiply':
   result = num1 * num2
  elif operation == 'divide':
    if num2 > 0:
        result = num1/num2
    else:
        result = "Cannot divide by zero"
  return result