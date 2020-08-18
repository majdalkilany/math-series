
def fibonacci(n) :
    '''
this function to calculate fibonacci series 
n= the number that we need to calculate fibonacci seris to it 
    '''
if n <=0 :
        return 'plese the number must more than 0'
    elif n == 1 :
        return 0
    elif n ==2 :
        return 1 
    else :
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n) :

    '''
    this function to calculate lucas series 
n= the number that we need to calculate lucas seris to it 

    '''
    if n <=0 :
        return 'plese the number must more than 0'
    elif n == 1 :
        return 2
    elif n ==2 :
        return 1 
    else :
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n2=0 ,n3=1) :
'''
    this function to calculate any  series where 
n= the number that we need to calculate the  seris to it 
n2 ==> the index number 1 for this series 
n3 ==> the index number 2 for this series 

'''
    # this is the base
        # if n2 == 0 and n3 == 1 :
    if n <=0 : 
         return 'plese the number must more than 0'
    elif n == 1 :
         return n2 
    elif n ==2 :
         return n3
    else :
         return sum_series(n-1,n2,n3) + sum_series(n-2,n2,n3)
            

