# Day 4: Marks Calculator using Function, Loop, and Exception Handling

# Function to insert valid marks for each subject
def insert_correct_mark(subject_name):
    while True:
        try:
            mark = int(input(f"Enter the marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid marks! Please enter a value between 0 to 100.")
        except ValueError:
            print("Please enter a number.")

# Input marks using function
math = insert_correct_mark("Math")
science = insert_correct_mark("Science")
english = insert_correct_mark("English")
computer = insert_correct_mark("Computer")

# Calculate total and percentage
marks = math + science + english + computer
percentage = marks / 4

# Output
print(f"\nTotal Marks: {marks}")
print(f"Percentage: {percentage:.2f}%")

# Result
if percentage >= 40:
    print("Congratulations! You passed.")
else:
    print("Sorry! You failed.")
