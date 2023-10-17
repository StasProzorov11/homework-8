# Написати валідації за допомогою регулярних виразів:

# - домашній номер телефону (тільки цифри та довжина номера)

# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)


# - домашній номер телефону (тільки цифри та довжина номера)

# import re
# def home_number(number):
#  pattern = re.compile(r'^\d{5,11}$')
#  return bool(pattern.match(number))

# home_num = "255255"
# print(home_number(home_num))


# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)

# import re
# def mobile_number(number):
#  pattern = re.compile(r'^\+?\d{10,15}$')
#  return bool(pattern.match(number))

# mobile_num = "+380999582212"
# print(mobile_number(mobile_num))


# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)

# import re
# def email(email):
#  pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$')
#  return bool(pattern.match(email))

# e_mail = "stasprozorov54@gmail.com"
# print(email(e_mail))


# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
# import re
# def validate_full_name(name):
#  pattern = re.compile(r'^[A-Za-zА-Яа-я-іІ-єЄ-їЇ-ґҐ]{2,20}\s[A-Za-zА-Яа-я-іІ-єЄ-їЇ-ґҐ]{2,20}\s[A-Za-zА-Яа-я-іІ-єЄ-їЇ-ґҐ]{2,20}$')
#  return bool(pattern.match(name))

# full_name = "Прозоров Станіслав Ігорович"
# print(validate_full_name(full_name))
