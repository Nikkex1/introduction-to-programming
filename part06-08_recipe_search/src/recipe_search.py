# Write your solution here
def search_by_name(filename: str, word: str):
    help_list = []
    recipe_list = []
    found_names = []
    with open(filename) as recipe_file:
        for line in recipe_file:
            line = line.strip()
            if line != "":
                help_list.append(line)
            if line == "":
                recipe_list.append(help_list)
                help_list = []
        recipe_list.append(help_list)

    for sublist in recipe_list:
        if word.lower() in sublist[0].lower():
            found_names.append(sublist[0])

    return found_names

def search_by_time(filename: str, prep_time: int):
    help_list = []
    recipe_list = []
    found_names = []
    with open(filename) as recipe_file:
        for line in recipe_file:
            line = line.strip()
            if line != "":
                help_list.append(line)
            if line == "":
                recipe_list.append(help_list)
                help_list = []
        recipe_list.append(help_list)

    for sublist in recipe_list:
        if int(sublist[1]) < prep_time:
            found_names.append(f"{sublist[0]}, preparation time {sublist[1]} min")

    return found_names

def search_by_ingredient(filename: str, ingredient: str):
    help_list = []
    recipe_list = []
    found_names = []
    with open(filename) as recipe_file:
        for line in recipe_file:
            line = line.strip()
            if line != "":
                help_list.append(line)
            if line == "":
                recipe_list.append(help_list)
                help_list = []
        recipe_list.append(help_list)

    for sublist in recipe_list:
        if ingredient in sublist[2:]: #only this line is different from previous
            found_names.append(f"{sublist[0]}, preparation time {sublist[1]} min")

    return found_names

if __name__ == "__main__":
    found_recipes = search_by_name("recipes2.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
