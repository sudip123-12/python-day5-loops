name=input("Enter your name: ") 
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in meters: "))
BMI=weight/(height*height)
print(f"Hello {name}, your BMI is {BMI:.2f}")
if(BMI<18.5):
    print("you are in underweight category")
elif(18.5<=BMI<25):
    print("you are in normal weight category")    
elif(25<=BMI<30):
    print("you are in overweight category")  
elif(BMI>=30):
    print("you are in obese category") 
       