# first_name = input('Enter your first name ')
#
# if first_name == "" or first_name is None:
#     print('Your first name cannot be empty')
#     exit()
# else:
#     last_name = input('Enter your last name')
# if last_name == "":
#     print('Your last name cannot be empty')
# else:
#     age = int(input('Enter your age'))
#     print('Your name is ', first_name, last_name)
# if age < 0:
#     print('Age cannot be negative')
# elif age < 18:
#     print('You are an underage')
# elif age > 65:
#     print('You are an old citizen')
# else:
#     print('You are a youth')




passes = 0
failures = 0
counter = 0
for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
    if result == 2:
        failures = failures +2
    if result != 1 or 2:
        continue
else:
    print('Passed:', passes)
    print('Failed:', failures)
# counter = counter + 1
# if counter == 10:
#     print(counter)