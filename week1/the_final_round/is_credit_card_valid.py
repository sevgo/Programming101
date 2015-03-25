from to_digits import to_digits


def is_credit_card_valid(number):
    old_numbers = to_digits(number)
    if len(old_numbers) % 2 == 0:
        return False

    doubled_odd_numbers = []
    for index in range(0, len(old_numbers)):
        doubled_odd_numbers.append(old_numbers[index] * 2 if index % 2 != 0 else old_numbers[index])

    new_numbers = ""
    for i in doubled_odd_numbers:
        new_numbers += str(i)

    verify_numbers = to_digits(int(new_numbers))

    if sum(verify_numbers) % 10 != 0:
        return False
    
    return True


if __name__ == "__main__":
    print (is_credit_card_valid(79927398715))
