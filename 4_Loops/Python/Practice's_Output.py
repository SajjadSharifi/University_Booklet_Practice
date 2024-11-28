from PracticesFunction import Excersises
from Tools import Tools

try:
    print("wellcome to bmm operation. pls enter 2 number")
    numbers = input("pls enter number like (1 2) in one line with space: ").split()
    numbers = Tools.StringListToInt(numbers)
    Excersises.Bmm(numbers[0], numbers[1])

    print("\n", "wellcome to strongNumberOperation. pls enter your numbers in one line!")
    number2 = input("pls enter your number: ")
    Excersises.IsStrongNumber(number2)
 
    print("\n", "wellcome to find sinx operation pls enter 2 number one for x and one for n in oneline :-) ")
    numbers3 = input("pls enter your numbers: ").split()
    numbers3 = Tools.StringListToInt(numbers3)
    Excersises.Sinx(n= numbers3[0], x= numbers3[1])
   
    print("\n", "wellcome to compelete Number Finder opration. ")
    number4 = int(input("pls enter your number: "))
    Excersises.CompeleteNumber(number4)
    
    print("\n", "wellcome to pi opration pls enter your 2 number in oneline the first one is for count and otherone is x value ")
    numbers5 = input("pls enter your numbers: ").split()
    numbers5 = Tools.StringListToInt(numbers5)
    Excersises.Pi(n= numbers5[0], x= numbers5[1])
    
except Exception as exception:
    raise exception("something went wrong")

finally:
    input("press any key to contineu ....")