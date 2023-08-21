def fibnacci(num):
    List_fib=[0,1]
    while len(List_fib)<num:
        Next_fib=List_fib[-1]+List_fib[-2]
        List_fib.append(Next_fib)
    return List_fib
n=int(input("Enter the term of Fibnacci Series is:"))
if n<=0:
    print("Please enter positive number")
else:
    data=fibnacci(n)
    print("Fibnacci series is: ",data)
