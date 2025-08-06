'''
def factorial():
    n = int(input('Enter a number: '))
    fact_n = 1
    for i in range(1,n+1):
        fact_n = fact_n * i
    print('factorial of',n,'is:',fact_n)
factorial()
'''

'''
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print('factorial of',n,'is:',fact)
    
factorial(0)
'''

def factorial(n):      
    if n < 2:
        result = 1
        print('factorial of',n,'is:',result)
        return result    
    else:
        result =  n * factorial(n-1)
        print('factorial of',n,'is:',result)
        return result
factorial(5)

