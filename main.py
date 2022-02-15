'''Bela  teaches her daughter  to find the factors of a given number.  When she provides a number to her daughter, she should tell the factors of that number.  Help her to do this, by writing a program.  Write a class FindFactor.java and write the main method in it.
Note :

If the input provided is negative, ignore the sign and provide the output. If the input is zero
If the input is zero the output should be “No Factors”.'''
a=int(input())
n=abs(a)
l=[]
if n<0 or n>0:
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print(*l,sep=",")
else:
    print("No factors")
