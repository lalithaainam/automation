first_number = 1
second_number = 2
print(first_number)
print(second_number)
result = 0
sum = 2
while first_number + second_number <= 1000:
    result = first_number + second_number
    print(result)
    if result % 2 == 0:
        sum = sum + result
    first_number = second_number
    second_number = result
print(sum)