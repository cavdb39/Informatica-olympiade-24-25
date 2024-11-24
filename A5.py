# Handle input
N = int(input())
operation = input()

# Construct list
cards = [i for i in range(1, 2 * N + 1)]

# Initiate variables
split_operation = []
shuffled_cards = []
temp = ""
processed_operation = ""

# Splitting the input
for char in operation:
    if char.isdigit() and (temp and not temp[-1].isdigit() and temp[-1] != "("):
        split_operation.append(temp)
        temp = ""
    temp += char

split_operation.append(temp)

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

        if start_index + 1 == end_index:
            remaining = text[1:] if len(text) > 1 else ""
            processed_operation += num * text[0] + remaining
        else:
            a = text[start_index + 1 : end_index]
            b = text[end_index + 1 :]

            for char in a:
                if not char.isdigit():
                    index_2 = a.index(char)
                    break

            if index_2:
                remaining = a[index_2 + 1 :] if index_2 + 1 < len(a) else ""
                a = int(a[:index_2]) * a[index_2] + remaining
            else:
                a[index_2]

            processed_operation += num * a + b
    else:
        remaining = text[1:] if len(text) > 1 else ""
        processed_operation += num * text[0] + remaining

for char in processed_operation:
    if char not in {"b", "r", "l"}:
        print("skipping invalid mode:", char)
        continue

    if char == "b":
        cards.append(cards.pop(0))
        continue
    else:
        left_part, right_part = cards[:N], cards[N:]
        if char == "r":
            shuffled_cards.extend(
                [card for pair in zip(left_part, right_part) for card in pair]
            )
        elif char == "l":
            shuffled_cards.extend(
                [card for pair in zip(right_part, left_part) for card in pair]
            )
        cards = shuffled_cards
        shuffled_cards = []

print(cards)
