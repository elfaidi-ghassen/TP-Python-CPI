def is_prime(n):
    if n < 2: return False
    return len([k for k in range(2, n) if n % k == 0]) == 0
while True:
    number = int(input("type a number: "))
    if number % 2 == 0:
        break

for i in range(1, number // 2):
    if is_prime(i) and is_prime(number - i):
        print(f"{i} + {number - i} = {number}")
        break

        

