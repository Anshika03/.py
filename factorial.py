#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Anshika
#
# Created:     23-12-2018
# Copyright:   (c) Anshika 2018
# Licence:     <your licence>
#---------------------------------------------------------------------------
a=(int(input("Enter the number")))
if (a<0):
    print("factorial does not exist")
elif(a== 0 or a==1):
    print("factorial of ",a,"is:-",1)
else:
        fact=1
        for i in range(2,a+1):
         fact*=i
        print("factorial of ", a,"is:-",fact)
