def calculate_grade():
    subjects = ["Python", "C Programming", "Mathematics", "Physics"]
    marks = []
    for subject in subjects:
        mark = float(input(f"Enter the marks in {subject}: "))
        marks.append(mark)
    total = sum(marks)
    aggregate = total / len(marks)
    if aggregate > 75:
        grade = "DISTINCTION"
    elif 60 <= aggregate < 75:
        grade = "FIRST DIVISION"
    elif 50 <= aggregate < 60:
        grade = "SECOND DIVISION"
    elif 40 <= aggregate < 50:
        grade = "THIRD DIVISION"
    else:
        grade = "FAIL"
    print(f"Total: {total}")
    print(f"Aggregate: {aggregate:.1f}")
    print(f"Grade: {grade}")
calculate_grade()