username="Gugulethu"
password="12345"
user1=input("Enter username:")
user2=input("Enter password:")
if username=="user1" and password=="user2":
    print(f"Login successful")
else:
    attempt =3
    while attempt>0:
        print("Login failed. Try again.")
        user1=input("Enter username:")
        user2=input("Enter password:")
        if username=="user1" and password=="user2":
            print("Login successful")
            break
        attempt -=1
        print(f"You have {attempt} attempts left.")

        


