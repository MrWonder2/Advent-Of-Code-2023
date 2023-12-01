f = open("input.txt")


lines = f.readlines()

nums_text = ['one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']
nums_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
             'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
sum = 0
for line in lines:
    num = []
    front = ""
    back = ""

    # front character

    for char in line:
        front += char
        if char.isdigit():
            num.append(int(char))
            break
        else:
            for number in nums_text:
                if number in front:
                    num.append(int(nums_dict[number]))
                    break
        if len(num) == 1:
            break

    for i in range(len(line), 0, -1):
        back = line[i-2]+back
        if line[i-2].isdigit():
            num.append(int(line[i-2]))
            break
        else:
            for number in nums_text:
                if number in back:
                    num.append(int(nums_dict[number]))
                    break
        if len(num) == 2:
            break

    sum = sum + num[0]*10 + num[-1]


print(sum)
