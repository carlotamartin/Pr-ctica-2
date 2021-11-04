def staircase(n):
    asteriscos = 1
    # Write your code here
    for espacios in range(n, 0, -1):
        for i in range (espacios):
            print(' ', end='')
        for j in range(asteriscos):
            print('*', end='')
        print()
        asteriscos+=2


staircase(7)
