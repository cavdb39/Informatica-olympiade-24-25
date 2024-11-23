start_num = int(input("Enter number: "))

print(type(start_num))

def nio_value(num: int):
    digits = [int(d) for d in str(num)]
    value = 0
    for i in range(len(digits)):
        value += (i + 1) * digits[i]
    return value

old_value = start_num
new_value = nio_value(old_value)

while True:
    if new_value == old_value:
        print(new_value)
        break
    old_value = new_value
    new_value = nio_value(old_value)
