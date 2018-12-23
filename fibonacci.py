#-------------------------------------------------------------------------------
# Name:        module3
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
d=(int(input("Enter a number")))
t1=0
t2=1
nextterm=0
print("0")
for i in range(0,d):
    nextterm=t1+t2
    t1=t2
    t2=nextterm
    print(nextterm)
    i=i+1

