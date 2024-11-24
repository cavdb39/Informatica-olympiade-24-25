def shuffle(mode: str):
    global cards
    if mode == "b":
        cards.append(cards.pop(0))
        return
    shuffled_cards = []
    left_part, right_part = cards[:N], cards[N:]
    print(left_part, right_part)
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
full_operation = input()

# Construct list
cards = [i for i in range(1, 2 * N + 1)]
print(cards)
