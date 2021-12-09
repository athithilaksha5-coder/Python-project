def creditcard_validator(card_number):
    last_digit = card_number[-1]
    r = card_number[-2::-1]
    number = ""
    for i in range(len(r)):
        if i % 2 == 0:
            n = int(r[i])*2
            if n > 9:
                n=n-9
                number += str(n)
            else:
                number += str(n)
        else:
            number += r[i]

    result = int(last_digit)
    for n in number:
        result += int(n)
    return print("valid credit card") if result % 10 == 0 else print("Invalid credit card")

card_number = input("Enter credit card number: ").strip()
creditcard_validator(card_number)