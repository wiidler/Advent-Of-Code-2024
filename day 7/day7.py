def isValidPart1(answer, numbers):
    tree = [[numbers[0]]]
    for i in range(1, len(numbers)):
        newTree = []
        for branch in tree:
            newTree.append(branch + [branch[-1] + numbers[i]])
            newTree.append(branch + [branch[-1] * numbers[i]])
        tree = newTree
    for branch in tree:
        if branch[-1] == answer:
            return True
    return False


def part1(input):
    validSolutions = []
    for line in input:
        answer = line[0]
        numbers = line[1]
        if isValidPart1(answer, numbers):
            validSolutions.append(answer)
    return sum(validSolutions)


def isValidPart2(answer, numbers):
    tree = [[numbers[0]]]
    for i in range(1, len(numbers)):
        newTree = []
        for branch in tree:
            newTree.append(branch + [branch[-1] + numbers[i]])
            newTree.append(branch + [branch[-1] * numbers[i]])
            newTree.append(branch + [int(str(branch[-1]) + str(numbers[i]))])
        tree = newTree
    for branch in tree:
        if branch[-1] == answer:
            return True
    return False


def part2(input):
    validSolutions = []
    for line in input:
        answer = line[0]
        numbers = line[1]
        if isValidPart2(answer, numbers):
            validSolutions.append(answer)
    return sum(validSolutions)


def parseInput():
    with open("./input.txt", "r") as file:
        input = file.read().strip().split("\n")
    result = []
    for line in input:
        parts = line.split(":")
        number = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))
        result.append([number, numbers])
    return result


def main():
    input = parseInput()
    answer1 = part1(input)
    answer2 = part2(input)
    print(f"Answer 1: {answer1}")
    print(f"Answer 2: {answer2}")


main()
