# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError
    if " " not in name:
        raise ValueError
    if len(name) > 40:
        raise ValueError
    if age < 0 or age > 150:
        raise ValueError
    
    return (name, age)

if __name__ == "__main__":
    print(new_person("Niklas LastName", 28))