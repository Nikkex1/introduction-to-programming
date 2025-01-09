# Write your solution here
password = input("Password:")
while True:
    password2 = input("Repeat password:")
    if password != password2:
        print("They do not match!")
    else:
        break
print("User account created!")