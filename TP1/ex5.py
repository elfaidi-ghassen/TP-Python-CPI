while True:
    number = int(input("type a number: "))
    if number > 0:
        break

divisors = [i for i in range(1, number) if number % i == 0]
if number == sum(divisors):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

