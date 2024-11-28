import math as Math
from Tools import Tools

class Excersises: 
    
    @staticmethod
    def Pi(x: int, n:int):
        if isinstance(x,int) and isinstance(n,int):   
            p = 0
            for i in range(n):
                p += (Math.exp(-x)) * ((x**i)/ Math.factorial(i))
            print(p)
        else:
            raise ValueError("pls enter valid number") 
    
    @staticmethod 
    #پیدا کردن عدد کامل
    def CompeleteNumber(number: int):
        if isinstance(number,int): 
            divisors = Tools.FindNmberDivisors(number)
            if sum(divisors) == number:
                print("this is a compelete number")
            else:
                print("this is note a compelete number!!!!")
                
    @staticmethod 
    # تشخیص اینکه عدد داده شده استرانگ است یا نه
    def IsStrongNumber(number:str):
        if isinstance(number,str):
            myNumber = 0
            for i in number:
                myNumber+= Math.factorial(int(i))
            if myNumber == int(number):
                print("your number is a strong number")
            else:
                print("sorry :-)")
    
    @staticmethod
    #پیدا کردن ب.م.م
    def Bmm(number1:int, number2:int):
        if isinstance(number1, int) and isinstance(number2,int):
            #بدست آوردن تمام اعدادی که دو عدد داده شده بر آنها بخش پذیراند
            rootsOfNumber1 = Tools.FindRootsOfNumber(number1)
            rootsOfNumber2 = Tools.FindRootsOfNumber(number2)
            # پیدا کردن مقادیر مشترک در دو تابع
            commonRoots = list()
            for a in rootsOfNumber1:
                for b in rootsOfNumber2:
                    if a == b:
                        commonRoots.append(a)

            # بزرگ ترین مقسوم علیه مشترک میشه ب.م.م ما اگرم مشترک با هم نداشتند میشه 1
            if len(commonRoots) != 0:
                print(max(commonRoots))
            else:
                print("BMM is 1")        
    
    #پیدا کردن سینوس با استفاده از فرمول سری
    @staticmethod
    def Sinx(n:int, x:int):
        sin = 0
        multiple = 1
        for i in range(n):
            if (i+1) % 2 != 0:
                sin += (x**multiple) / Math.factorial(multiple)
            elif (i+1) % 2 == 0:
                sin -= (x**multiple) / Math.factorial(multiple)    
            multiple +=2
        print(sin)
        