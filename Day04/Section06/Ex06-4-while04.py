'''
파일명 : Ex06-4-while04.py
'''
dan = 2
while dan <= 9:
    n = 1
    while n <= 9:
        print('{}x{}={} '.format(dan, n, dan*n), end='')
        n += 1
    dan += 1
    print()

    ##중첩 while문