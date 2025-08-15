def get_valid_mark(subject_name):
    while True:
        try:
            mark = int(input(f"Enter marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter numbers only, not letters.")

math = get_valid_mark("Math")
science = get_valid_mark("Science")
english = get_valid_mark("English")
nepali = get_valid_mark("Nepali")
computer = get_valid_mark("Computer")

total = math + science + english + nepali + computer
percentage = total / 5

print(f"\nTotal marks: {total}")
print(f"Percentage: {percentage:.2f}%")

