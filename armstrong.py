'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


n=int(input("enter the number"))
original=n


num=n
count=0
while(n>0):
    n=n//10
    count+=1


armstrong_num=0
while num>0:
    armstrong_num = armstrong_num + (num%10)**count
    num=num//10
    
    
if original==armstrong_num:
    print("the number is armstrong ")
    
else:
    print("the number is not armstrong")

    
    
