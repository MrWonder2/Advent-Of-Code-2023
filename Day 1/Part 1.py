f = open("input.txt")


lines = f.readlines()


sum = 0
for line in lines:
    num = []
    for char in line:
        if char.isdigit():
            num.append(int(char))
    sum = sum + (num[0]*10 + num[-1])

print(sum)
