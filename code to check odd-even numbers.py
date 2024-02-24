
'''
"Given an integer, , perform the following conditional actions:

"If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird"
'''

if __name__ == '__main__':
    n=int(input("please provide a number between 1 and 100: "))
if n%2 != 0 :
    print('Weird')
elif 2<=n<=5 :
    print("Not Weird")
elif 6<=n<=20 :
    print('Weird')
elif n>20:
    print('Not Weird')

