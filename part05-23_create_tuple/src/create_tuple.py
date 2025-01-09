# Write your solution here
def create_tuple(x: int, y: int, z:int):
    templist = [x, y, z]
    templist.sort()
    
    t = (templist[0], templist[2], sum(templist))
    return t

if __name__ == "__main__":
    print(create_tuple(1, 4, 2))
