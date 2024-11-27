from PracticeFunction import  ExercisesMethods as exerciseMethods

try:       
    print("Wellcome to Show Practice result programm")
    print("now we want to convert cels into farenhite")

    degree = int(input("pls enter your cels degree: "))
    exerciseMethods.ConvertCelsIntoFarenhit(degree)

    print("now we will find triangle area by using it's sides")
    triangleSidesList = input("you must enter your numbers like this: 1,2,3,4: ").split(",")

    exerciseMethods.FindAreaByTriangleSides(triangleSidesList)

   
except Exception as exception:
    raise exception("something went wrong")

finally:
     input("press any key to continue....")
    
    
    
    
    