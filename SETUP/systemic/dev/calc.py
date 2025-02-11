# calc.py
def calc_command(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    expression = input("Enter the expression to calculate: ")
    calc_command(expression)