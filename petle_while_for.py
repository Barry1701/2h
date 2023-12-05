# number = 1
# while number < 6:
#     print(number)
#     number += 1

for number in range(9):
    if number == 5:
        continue # omija
    print(number)

for number in range(9):
    if number == 5:
        break # przerywa
    print(number)