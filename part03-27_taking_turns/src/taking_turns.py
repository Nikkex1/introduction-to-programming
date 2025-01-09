# Write your solution here
limit = int(input("Please type in a number:"))
maxn = limit
minn = 1
count = 0

while count <= limit:
    print(minn)
    count += 1
    minn += 1
    if count >= limit:
        break
    print(maxn)
    count += 1
    maxn -= 1
    if count >= limit:
        break