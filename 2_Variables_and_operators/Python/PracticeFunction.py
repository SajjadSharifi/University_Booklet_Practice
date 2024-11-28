import math as Math

class ExercisesMethods():
    @staticmethod
    def FindAreaByTriangleSides(triangleSides:list):
     try:
        # باید 3 تا مقدار وارد کنه
        # اگر 3 تا ضلع وارد نکرد باید ارور بده
        # شرط مثلث بودن رو چک میکنیم
        if len(triangleSides)!=3:
            raise Exception()
        
        triangleSidesInt = list()
        
        for i in triangleSides:
            triangleSidesInt.append(int(i))

        if ((triangleSidesInt[0] + triangleSidesInt[1] > triangleSidesInt[2]) and 
            triangleSidesInt[2] + triangleSidesInt[0] > triangleSidesInt[1] and
            triangleSidesInt[1] + triangleSidesInt[2] > triangleSidesInt[0]):
                    
                # بدست آوردن محیط 
            p = (triangleSidesInt[0] + triangleSidesInt[1] + triangleSidesInt[2]) /2
                    
                # بدست آوردن مساحت با داشتن اضلاع
            s =  Math.sqrt(p*(p-triangleSidesInt[0])*(p-triangleSidesInt[1])*(p-triangleSidesInt[2]))
            print(s)
           
        else:
            print("sorry the numbers you get to me wont make a triangle")
                
     except Exception as exception:
        exception("something went wrong in FindAreaByTriangleSides Method!")
    
    @staticmethod
    def ConvertCelsIntoFarenhit(degree: int):
        try:
         # میخواهی سیلسیوس رو به فارنهایت تبدیل کنیم
         if isinstance(degree, int):   
            print(f"The Answer is: {(degree * 1.8) + 32}")
         else:
             raise ValueError("string is not recomended")
        except ValueError:
            print("pls enter string number")

        