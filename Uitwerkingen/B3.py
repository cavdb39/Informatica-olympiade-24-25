from itertools import combinations

words = [
    "niet",
    "langer",
    "als",
    "ik",
    "dood",
    "zal",
    "zijn,",
    "dan",
    "dat",
    "je",
    "diep",
    "de",
    "doodsklok",
    "nog",
    "hoort",
    "slaan",
    "die",
    "tot",
    "de",
    "wereld",
    "spreekt",
    "over",
    "mijn",
    "eind:",
    "de",
]

lowest_score = 100000
max_newlines = 9
targeted_index = None


def evaluate_points(configurations: list):
    global lowest_score
    for text in configurations:
        score = 1000
        valid = True

        sentence = " ".join(text[-1])
        if len(sentence) > 15:
            continue

        for row in text[:-1]:
            sentence = " ".join(row)
            score += 1000 + (15 - len(sentence)) ** 2

            if len(sentence) > 15 or not valid:
                valid = False
                break

        if valid and (score < lowest_score):
            lowest_score = score
            print("Found new lowest score of", score)
            print("Rows:\n", "\n".join([" ".join(row) for row in text]))


def generate_permutations(newlines: int):
    all_configurations = []
    newline_positions = combinations(range(24), newlines + 1)
    for positions in newline_positions:
        current_row = []
        line = []
        for idx in range(24):
            line.append(words[idx])

            if idx in positions:
                current_row.append(line)
                line = []

        if line:
            line.append(words[24])
            current_row.append(line)

        all_configurations.append(current_row)
    return all_configurations


for i in range(1, max_newlines):
    print(f"Evaluating configurations with {i} newlines:")
    evaluate_points(generate_permutations(i))

print("Lowest score found overall:", lowest_score)
