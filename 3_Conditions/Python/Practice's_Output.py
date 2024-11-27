from PracticesFunction import Exercises

try:
    #مراحل bmi
    print("wellcome to bmi process")
    weight = int(input("pls enter your weight: "))
    height = int(input("pls enter your height: "))
    Exercises.BMI(height= height, weight= weight)
    
    # معادله درجه 2
    print("wellcome to SecondDegreeEquation process")
    print("pls enter your variable's coeffientes like 1 2 3")
    
    # برای راحتی متغیر ها رو توی یک لیست ذخیره میکنیم و بعد تبدیل به عدد میکنیم
    variablesCoeffiente = input().split()
    intVariables = list()
    
    # تبدیل لیست رشتمون به عدد
    for i in variablesCoeffiente:
        intVariables.append(int(i))
        
    # ست کردن متغیر ها به تابعمون
    Exercises.SecondDegreeEquation(intVariables[0], intVariables[1], intVariables[2])
    
    #تابع پیدا کردن فاصله بین دو تاریخ با روز های بینشون
    print("wellcome to DistanceBetweenDates process")
    date1 = input("pls enter your date as 8 digit number: ")
    date2 = input("pls enter your date as 8 digit number: ")

    Exercises.DistanceBetweenDates(date1= date1, date2= date2)
    

except Exception as exception:
    raise exception("Something went wrong")

finally:
    input("press any Key to continue")
