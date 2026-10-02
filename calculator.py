import time


def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  if b == 0:
    return "Error: Division by zero!"
  return a / b


def calculator():
  print("--- Python Basic Calculator ---")
  print("Select operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")

  choice = input("Enter choice (1/2/3/4): (default 1): ").strip()
  if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Defaulting to Addition.")
    choice = "1"

  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    return

  # Measure execution time of the calculation
  start_time = time.perf_counter()

  if choice == "1":
    result = add(num1, num2)
    op = "+"
  elif choice == "2":
    result = subtract(num1, num2)
    op = "-"
  elif choice == "3":
    result = multiply(num1, num2)
    op = "*"
  elif choice == "4":
    result = divide(num1, num2)
    op = "/"

  end_time = time.perf_counter()
  execution_time = (end_time - start_time) * 1000  # Convert to milliseconds

  print(f"\nResult: {num1} {op} {num2} = {result}")
  print(f"Calculation Execution Time: {execution_time:.6f} milliseconds")


if __name__ == "__main__":
  calculator()