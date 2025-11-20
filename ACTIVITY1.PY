def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")

def get_operator():
    ops = ['+', '-', '*', '/', '%', '**']
    prompt = "Choose an operator (" + " ".join(ops) + "): "
    while True:
        op = input(prompt).strip()
        if op in ops:
            return op
        print("Invalid operator. Choose one of:", ", ".join(ops))

def calculate(a, b, op):
    try:
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b
        if op == '%':
            return a % b
        if op == '**':
            return a ** b
    except ZeroDivisionError:
        return "Error: Division by zero"

def format_result(r):
    if isinstance(r, (int, float)):
        if isinstance(r, float) and r.is_integer():
            return str(int(r))
        return str(r)
    return str(r)

def main():
    print("Simple calculator (enter numbers, choose operator)")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    op = get_operator()
    result = calculate(a, b, op)
    print("Result:", format_result(result))

if __name__ == "__main__":
    main()
