#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anshika
#
# Created:     22-12-2018
# Copyright:   (c) Anshika 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
    a=(int(input("enter the number")))
    b=(int(input("enter the number")))
    c=(int(input("enter the number")))

    if (a>b) and (a>c):
     print("a is the greatest number")
    elif (b>a) and (b>c):
     print ("b is the greatest number")
    else:
     print("c is the greatest number")


