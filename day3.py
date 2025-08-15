#code for input name and marks and know the grade
name=input("Enter your name: ")
a=int(input("Enter your marks: "))

if(90<=a<=100):
    print("hello",name,"you got grade A+")
elif(80<=a<=89):
    print("hello",name,"you got grade A") 
elif(70<=a<=79):
    print("hello",name,"you got grade B")  
elif(60<=a<=69):
    print("hello",name,"you got grade C")      
elif(50<=a<=59):
    print("hello",name,"you got grade D")    
elif(0<=a<50):
    print("hey",name,"you are fail") 
else:
    print("hello",name,"Invalid marks!, please give me a number between 1 to 100")       