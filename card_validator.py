def main(card_number):
    card_translate = str.maketrans({'-': '', ' ': ''})
    translated_card = card_number.translate(card_translate)
    sum_odd = 0
    card_rev = translated_card[::-1]
    odd_digits = card_rev[::2]

    for i in odd_digits:
        sum_odd += int(i)
    sum_even = 0
    even_digits = card_rev[1::2]

    for number in even_digits:
        number = int(number) * 2
        if number >= 10:
            sum_even += (number // 10 + number % 10)
        else:
            sum_even += number
    final = sum_even + sum_odd
    if (final % 10) == 0:
        print('VALID! ')
    else:
        print('INVALID!')
        
card_number = input('Write your card number seperate with - or with space ')

main(card_number)