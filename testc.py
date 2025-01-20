number1 = int(input("Enter a number (or 'DONE' to End):"))
list1 = []

while number1 != "DONE":
        number2 = int(input("Enter a number (or 'DONE' to End):"))
        number2 = number2
        
        number_3 = number1% number2
        
        while number_3 == 0:
                list1.append(number1)
        num4 = number2 % number2
        while  num4 == 0:
                list1.append(number2)
        