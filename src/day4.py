# Day 4 puzzles
def adjacent_rule(number):
    count = 0
    for num_1, num_2 in zip(number, number[1:]):
        if num_1 == num_2:
            count += 1
        else:
            if count == 1:
                return True
            count = 0
    return count == 1


def check_repeat(number):
    for digit1, digit2 in zip(number, number[1:]):
        if digit1 == digit2:
            return True


def order_rule(number):
    return "".join(sorted(number)) == number


def possible_passwords():
    count = 0
    for num in range(138307, 654504):
        num = str(num)
        if order_rule(num):
            if check_repeat(num):
                count += 1
    return count


def different_passwords():
    count = 0
    for num in range(138307, 654504):
        num = str(num)
        if order_rule(num):
            if adjacent_rule(num):
                count += 1

    return count


print(possible_passwords())
print(different_passwords())
