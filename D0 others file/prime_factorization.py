import math

number = int(input("Type a number: "))

def factorization(num):
    # 確認是不是質數
    def is_prime(num1):
        for i in range(2, int(math.sqrt(num1))):
            if num1 % i == 0:
                return False
        return True

    def reduction(num2):
        for i in range(2, num2):
            if num2 % i == 0:
                power = 0
                print(i, end="^")
                while num2 % i == 0:
                    power += 1
                    num2 /= i
                print(power, end=' ')

    if is_prime(num):
        print(f"{num} = 1 * {num}")
    else:
        reduction(num)


factorization(number)
