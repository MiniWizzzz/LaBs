
def laB_4_4() -> bool:

    number = input("Введите номер билета: ")

    if len(number)<2 or (len(number)%2>0):
        print("Количество цифр в билетие должно быть четным!")
        return False

    digits = list(map(int, number))

    right_half = digits[:len(digits)//2]
    left_half = digits[len(digits)//2:]

    sum_right_half = sum(right_half)
    sum_left_half = sum(left_half)

    if sum(right_half) == sum(left_half):
        print("Счастливый билет")
    else:
        print("Несчастливый билет (грустный)")

print(laB_4_4())
