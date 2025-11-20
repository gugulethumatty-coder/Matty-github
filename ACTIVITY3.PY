def get_integer(prompt):
    while True:
        s = input(prompt).strip()
        # accept optional + or - followed by digits only
        if (s.startswith(('+','-')) and s[1:].isdigit()) or s.isdigit():
            return int(s)
        print("Invalid input. Please enter an integer.")

def main():
    n = get_integer("Enter an integer: ")
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

if __name__ == "__main__":
    main()
