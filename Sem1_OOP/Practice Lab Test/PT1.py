def sum_divisors(num: int):
    if num < 0:
        print("Negative number. Only positive numbers accepted")
        return
    output = ""
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
            output += str(i) + " + "

    print(output[:-3], "=", sum)


#main scope
sum_divisors(20)
sum_divisors(33)
sum_divisors(42)
sum_divisors(-1)
