number = int(input('enter a number :'))
index = 2
while index <= number//2:
    if number % index == 0:
        print(index)
    index = index + 1
