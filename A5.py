def shuffle(mode: str) -> list:
    if mode not in "brl":
        print(f"skipping invalid mode '{mode}'.")
        return
    global cards
    if mode == "b":
        cards.append(cards.pop(0))
        return
    shuffled_cards = []
    left_part, right_part = cards[:N], cards[N:]
    if mode == "r":
        for _ in range(N):
            shuffled_cards.append(left_part.pop(0))
            shuffled_cards.append(right_part.pop(0))
    elif mode == "l":
        for _ in range(N):
            shuffled_cards.append(right_part.pop(0))
            shuffled_cards.append(left_part.pop(0))
    cards = shuffled_cards


# Handle input
N = int(input())
operation = input()

# Construct list
cards = [i for i in range(1, 2 * N + 1)]

split_operation = []
temp = ""

processed_operation = ""

# Splitting the input
for char in operation:
    if char.isdigit():
        if temp and not (temp[-1].isdigit() or temp[-1] == "("):
            split_operation.append(temp)
            temp = ""
    temp += char

split_operation.append(temp)

print(split_operation)

# Process each task
for task in split_operation:
    has_digit = False
    for char in task:
        if not char.isdigit():
            first_letter_index = task.index(char)
            break
        else:
            has_digit = True

    if not has_digit:
        processed_operation += task
        continue

    num, text = int(task[:first_letter_index]), task[first_letter_index:]

    if "(" in text:
        start_index = text.find("(")
        end_index = text.find(")")

        a = text[start_index + 1 : end_index]
        b = text[end_index + 1 :]

        print(a)

        for char in a:
            if not char.isdigit():
                index_2 = a.index(char)
                break

        remaining = a[index_2 + 1 :] if index_2 + 1 < len(a) else ""
        if index_2:
            a = int(a[:index_2]) * a[index_2] + remaining
        else:
            a[index_2]

        processed_operation += num * a + b
    else:
        print(num, text)
        remaining = text[1:] if len(text) > 1 else ""
        print(remaining)
        processed_operation += num * text[0] + remaining

print(processed_operation)

for char in processed_operation:
    shuffle(char)

print(cards)
