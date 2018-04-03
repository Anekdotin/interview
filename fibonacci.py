import timeit


mycode = '''

def fbonacci(n):

    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b

    return a



for i in range(1,10000):
    print(i, ':', fbonacci(i))
    
'''
# timeit statement
print(timeit.timeit(
                    stmt = mycode,
                    number = 1))