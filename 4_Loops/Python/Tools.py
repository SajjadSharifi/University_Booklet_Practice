class Tools: 
    @staticmethod
    # بجز خود عدد ، بدست آوردن مضارب یک عدد
    def FindNmberDivisors(number: int):
        if isinstance(number, int):
            divisors = list()
            for i in range((number // 2) + 1):
                if i == 0:
                    continue
                if number% i == 0:
                    divisors.append(i)
            return divisors
        else:
            raise ValueError("pls enter a valid number")
    
    @staticmethod
    # بدست آوردن مضارب یک عدد و خود عدد
    def FindRootsOfNumber(number: int):
        if isinstance(number, int):
           roots = list()
           for i in range((number // 2) + 1):
               if i == 0:
                   continue
               if number%i == 0:
                    roots.append(i)
           roots.append(number)
           return roots   
    @staticmethod
    def StringListToInt(numbers: list):
        intedList = list()
        for i in numbers:
            intedList.append(int(i))
        return intedList