# Write your solution here
from string import ascii_uppercase
import operator

def run(program: list):
    #Pre-defined variables A-Z
    variables = {}
    for letter in ascii_uppercase:
        variables[letter] = 0

    #Operators as a dictionary
    operators = {
            "==": operator.eq,
            "!=": operator.ne,
            "<": operator.lt,
            "<=": operator.le,
            ">": operator.gt,
            ">=":operator.ge
            }

    #Results
    results = []

    #Commands
    step = 0

    while step < len(program):
    
        part = program[step]
        part = part.split()
        command = part[0]
        #print(f"step {step}; command {command}")

        if command == "PRINT": #PRINT value // part[0,1]
            if part[1] in ascii_uppercase:
                results.append(variables[part[1]])
            else:
                results.append(int(part[1]))

        elif command == "MOV": #MOV variable value // part[0,1,2]
            if part[2] in ascii_uppercase:
                variables[part[1]] = variables[part[2]]
            else:
                variables[part[1]] = int(part[2])

        elif command == "ADD": #ADD variable value // part[0,1,2]
            if part[2] in ascii_uppercase:
                addition = variables[part[1]] + variables[part[2]]
            else:
                addition = variables[part[1]] + int(part[2])
            variables[part[1]] = addition

        elif command == "SUB": #SUB variable value // part[0,1,2]
            if part[2] in ascii_uppercase:
                subtraction = variables[part[1]] - variables[part[2]]
            else:
                subtraction = variables[part[1]] - int(part[2])
            variables[part[1]] = subtraction

        elif command == "MUL": #MUL variable value // part[0,1,2]
            if part[2] in ascii_uppercase:
                multiplication = variables[part[1]] * variables[part[2]]
            else:
                multiplication = variables[part[1]] * int(part[2])
            variables[part[1]] = multiplication

        elif command == "JUMP": #JUMP location // part[0,1]
            location = program.index(f"{part[1]}:")
            step = location
            continue

        elif command == "IF": #IF X (== != < <= > >=) Y JUMP location // part[0,1,2,3,4,5]
            values = []
            if part[1] in ascii_uppercase:
                values.append(variables[part[1]])
            else:
                values.append(int(part[1]))
            if part[3] in ascii_uppercase:
                values.append(variables[part[3]])
            else:
                values.append(int(part[3]))

            func = operators[part[2]]
            if func(values[0],values[1]):
                location = program.index(f"{part[5]}:")
                step = location
                continue

        elif command == "END": #Finish execution
            return results

        step += 1

    return results #in case there is no END command

if __name__ == "__main__":

    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)