for num in range(100, 1000):
    sum = 0
    x = num

    while x > 0:
        digit = x % 10
        sum = sum + digit**3  
        x = x // 10

    if num == sum:
        print(num)
