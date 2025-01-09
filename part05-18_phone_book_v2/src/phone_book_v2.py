# Write your solution here
phonebook = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 1: #search
        search = input("name:")
        if len(phonebook) > 0:
            for key in phonebook:
                if key == search:
                    for phonenumbers in phonebook[key]:
                        print(phonenumbers)
                    break
            else:
                print("no number")
        else:
            print("no number")
    elif command == 2: #add
        name = input("name:")
        number = input("number:")
        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(number)
        #print(f"test: {phonebook}")
        print("ok!")
    elif command == 3: #quit
        print("quitting...")
        break