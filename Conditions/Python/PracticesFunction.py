import math as Math

class Exercises:
    @staticmethod
    def BMI(height: int, weight: int):
        if isinstance(height,int) and isinstance(weight, int):
            print(weight / Math.sqrt(height))
            
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