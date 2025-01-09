# Write your solution here
def oldest_person(people: list):
    ages = []
    for item in people:
        ages.append(item[1])

    ages.sort()
    
    for item in people:
        if min(ages) == item[1]:
            return(item[0])

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people_list = [p1, p2, p3, p4]

    print(oldest_person(people_list))