import math as Math
from Tools import Tools 

class Exercises:
    @staticmethod
    #تخمین bmi
    def BMI(height: int, weight: int):
        if isinstance(height,int) and isinstance(weight, int):
            print(weight / Math.sqrt(height))
    # حل معادله درجه 2   
     
    @staticmethod
    def SecondDegreeEquation(a: int,b: int ,c: int):
        # input ax^2 + bx + C 
        # we solve it with delta Way 
        if isinstance(a,int) and isinstance(b, int) and isinstance(c,int):

            if a == 0:
                raise ValueError("your equation is not 2nd degree equation")
            
            else:
                #else start
                delta = (b ** 2) - (4 * a * c)
                rootsOfEquation = list()
                
                # assigning the root's value
                if delta == 0:
                    rootsOfEquation.append((-b + Math.sqrt(delta)) / (2 * a))
                else:
                    for i in range(2):
                        if i ==0:
                            rootsOfEquation.append((-b + Math.sqrt(delta)) / (2 * a))
                        elif i == 1:
                            rootsOfEquation.append((-b - Math.sqrt(delta)) / (2 * a))

                # show the roots wheter is one or two
                for root in rootsOfEquation:
                    i = 1
                    print(f"Root{i} is: {root}")
                    i +=1
                #else end
                
    # مقدار پول لازم برای خرید مقدار محصول مورد نظر
    @staticmethod
    def PayValue(numberOfBuy: int):
        if (isinstance(numberOfBuy, int)):
            if numberOfBuy < 1000:
               print(f"you will buy each product {2400 * numberOfBuy}$")
            elif numberOfBuy > 1000 and numberOfBuy<= 2000:
               print(f"you will buy each product {(2400 * 1000) + ((numberOfBuy-1000)*2200)}$")
            elif numberOfBuy > 2000:
                print(f"you will buy each product {(2400 * 1000) + (1000 * 2200) + ((numberOfBuy -2000)*1900)}$")
     
    # پیدا کردن فاصله میان 2 تاریخ مختلف   
    # اگر تاریخ میخوای بدی باید دوتاش شمسی یا دوتاش میلادی باشه وگرنه درست کار نمیکنه!        
    @staticmethod
    def DistanceBetweenDates(date1: str, date2: str):
        if isinstance(date1, str) and isinstance(date2, str):
            
            # تاریخ رو ابتدا به یک لیست استرینگ تبدیل کرده سپس لیست رشته ایی را به لیست عددی تبدیل میکنیم
            formatedDate1 = Tools.dateToInt(Tools.dateFormatter(date1))
            # حالا لیست تاریخمون رو به روز تبدیل میکنیم
            numberOfDays1 = (formatedDate1[0] * 365) + (formatedDate1[1] * 30) + formatedDate1[2]
            
            formatedDate2 = Tools.dateToInt(Tools.dateFormatter(date2))
            numberOfDays2 = (formatedDate2[0] * 365) + (formatedDate2[1] * 30) + formatedDate2[2]
            # تعداد روز های باقی مونده 
            
            remainDays = abs(numberOfDays1 - numberOfDays2)
            #مقدار فاصله رو با تعداد روز ها مشخص میکنیم
            print(remainDays) 
            
