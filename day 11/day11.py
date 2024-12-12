from collections import defaultdict


def part1(input, blinks):
    counts = defaultdict(int)
    for num in input:
        counts[num] += 1

    for rounds in range(blinks):
        print(f"Round {rounds + 1}")
        newCounts = defaultdict(int)
        for num, count in counts.items():
            if num == "0":
                newCounts["1"] += count
            elif len(num) % 2 == 0:
                firstHalf = num[: len(num) // 2]
                secondHalf = num[len(num) // 2 :]
                firstHalf = str(int(firstHalf))
                secondHalf = str(int(secondHalf))
                newCounts[firstHalf] += count
                newCounts[secondHalf] += count
            else:
                newCounts[str(int(num) * 2024)] += count
        counts = newCounts

    total = sum(counts.values())
    return total


def parseInput():
    input = open("./input.txt", "r")
    input = input.read()
    input = input.split(" ")
    return input


def main():
    input = parseInput()
    answer1 = part1(input, 25)
    answer2 = part1(input, 75)
    print(f"Answer 1: {answer1}")
    print(f"Answer 2: {answer2}")


main()
