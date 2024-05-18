password_1 = input("Введите пароль: ")
password_2 = input("Подтвердите пароль: ")

SpecialSym=["!","?","#","$","%","@"]
val = True

if password_1 != password_2:
    print("Пароли не совпадают")
    val = False

if len(password_1) < 8:
    print("Пароль должен содержать минимум 8 символов")
    val = False

if len(password_1) > 16:
    print("Пароль должен содержать не более 16 символов")
    val = False

if not any(char.isdigit() for char in password_1):
    print("Пароль должен содержать хотя бы одну цифру")
    val = False

if not any(char.isupper() for char in password_1):
    print("Пароль должен содержать заглавные буквы")
    val = False

if not any(char.islower() for char in password_1):
    print("Пароль должен содержать строчные буквы")
    val = False

if not any(char in SpecialSym for char in password_1):
    print("Пароль должен содержать специальные символы")
    val = False

if val:
    print("Пароль подтвержден")
