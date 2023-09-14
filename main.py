# find amount of dividers and return list of dividers if count = 4
def find_dividers(n):
    dividers = []
    count = 0
    for i in range(1, int(n**(1/2) + 1)):
        if n % i == 0:
            dividers += i, n // i
            count += 2
            if i == n // i:
                count -= 1
    dividers = sorted(list(set(dividers)), reverse=True)
    # make set to remove duplicates
    if count == 4:
        return dividers


while True:
    a, b = input(), input()
    # check if a and b are numbers
    if a.isdigit() and b.isdigit():
        a, b = int(a), int(b)
        for j in range(a, b + 1):
            result = find_dividers(j)
            # result - list of dividers, if count == 4
            # result - None, if count != 4
            if result:
                print(f'{j}, dividers: {result}')
    else:
        print("Пожалуйста, введите натуральные числа")