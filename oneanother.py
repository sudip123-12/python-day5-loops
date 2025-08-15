name=input("Enter your name: ")
math=int(input("Enter the marks of math(0-100): "))
science=int(input("Enter the marks of science(0-100): "))
English=int(input("Enter the marks of english(0-100): "))
Computer=int(input("Enter the marks of computer(0-100): "))
Nepali=int(input("Enter the marks of nepali(0-100): "))

if not (0 <= math <= 100 and 0 <= science <= 100 and 0 <= English <= 100 and 0 <= Computer <= 100 and 0 <= Nepali <= 100):
    print(" Error: Marks should be between 0 and 100 only.")
else:
    marks = math+science+English+Computer+Nepali
    percentage=(marks/500)*100
    print(f"\nHello {name}, your total marks = {marks}.")
    print(f"your percentage = {percentage:.2f}%.")
    if(90<=percentage<=100):
        print("you got grade A+")
    elif(80<=percentage<=89):
        print("you got grade A")
    elif(70<=percentage<=79):
        print("you got grade B+")
    elif(60<=percentage<=69):
        print("you got grade B")
    elif(50<=percentage<=59):
        print("you got grade C+")
    elif(40<=percentage<=49):
        print("you got grade C")
    elif(percentage<40):
        print("you are fail")                   
            

 