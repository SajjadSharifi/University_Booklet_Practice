class Tools:
   # این بخش مربوط به ابزار آلاتی است که مجبور شدم برای پروژه طراحیشون کنم
   
    @staticmethod
    def dateFormatter(date: str):
        if isinstance(date, str):
            dateHolder = ""
            #تبدیل کردن عدد 8 رقمیمون به یک فرمت تاریخ
            for i in range(8): 
             dateHolder += date[i]
             if len(dateHolder) == 4:
                dateHolder+="/"
             elif len(dateHolder) == 7:
                dateHolder+="/"
            # it will return date as 1999/09/09
            return dateHolder
    
    @staticmethod
   #بتبدیل کردن یک تاریخ فرمت شده مثل 1403/01/03 به یک لیست عددی 
    def dateToInt(date: str):
        if isinstance(date, str):
            intedDate = list()
            intConvertorHolder = date.split("/")
            for a in intConvertorHolder:
               intedDate.append(int(a))
            return intedDate
            
    @staticmethod
    def DaysToDate(days:int):
        if isinstance(days,int):
            year = days // 365
            month = days // 30
            while month > 12:
                month-= 12
                #end while
            day = days % 30
            return f"{year:02}/{month:02}/{day:02}"          
                
    
