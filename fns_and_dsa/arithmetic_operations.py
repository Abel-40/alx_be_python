def perform_operation(num1, num2, operation):
  result = ""
  match operation:
    case 'add':
      result = num1 + num2
    case 'subtract':
      result = num1 - num2
    case 'multiply':
      result = num1 * num2
    case 'divide':
      if num2 == 0:
        result = "division by zero is undefined"
      elif num2 != 0:
        result = num1 / num2
  return result