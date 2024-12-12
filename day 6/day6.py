def part1(input):
    direction = "N"
    visited = set()
    moved = True
    while moved:
        moved = False
        for i in range(len(input)):
            if direction == "N":
                location = input[i].find("^")
                if location != -1:
                    visited.add((i, location))
                    if i - 1 < 0:
                        break
                    if input[i - 1][location] == "#":
                        direction = "E"
                        input[i] = input[i][:location] + ">" + input[i][location + 1 :]
                    else:
                        input[i] = input[i][:location] + "X" + input[i][location + 1 :]
                        input[i - 1] = (
                            input[i - 1][:location] + "^" + input[i - 1][location + 1 :]
                        )
                    moved = True
                    break
            elif direction == "E":
                location = input[i].find(">")
                if location != -1:
                    visited.add((i, location))
                    if location + 1 >= len(input[i]):
                        break
                    if input[i][location + 1] == "#":
                        direction = "S"
                        input[i] = input[i][:location] + "v" + input[i][location + 1 :]
                    else:
                        input[i] = input[i][:location] + "X" + input[i][location + 1 :]
                        input[i] = (
                            input[i][: location + 1] + ">" + input[i][location + 2 :]
                        )
                    moved = True
                    break
            elif direction == "S":
                location = input[i].find("v")
                if location != -1:
                    visited.add((i, location))
                    if i + 1 >= len(input):
                        break
                    if input[i + 1][location] == "#":
                        direction = "W"
                        input[i] = input[i][:location] + "<" + input[i][location + 1 :]
                    else:
                        input[i] = input[i][:location] + "X" + input[i][location + 1 :]
                        input[i + 1] = (
                            input[i + 1][:location] + "v" + input[i + 1][location + 1 :]
                        )
                    moved = True
                    break
            elif direction == "W":
                location = input[i].find("<")
                if location != -1:
                    visited.add((i, location))
                    if location - 1 < 0:
                        break
                    if input[i][location - 1] == "#":
                        direction = "N"
                        input[i] = input[i][:location] + "^" + input[i][location + 1 :]
                    else:
                        input[i] = input[i][:location] + "X" + input[i][location + 1 :]
                        input[i] = input[i][: location - 1] + "<" + input[i][location:]
                    moved = True
                    break
    return len(visited)


def part2(input):
    return


def parseInput():
    with open("./example.txt", "r") as file:
        input = file.read().strip().split("\n")
    return input


def main():
    input = parseInput()
    answer1 = part1(input)
    answer2 = part2(input)
    print(f"Answer 1: {answer1}")
    print(f"Answer 2: {answer2}")


main()
