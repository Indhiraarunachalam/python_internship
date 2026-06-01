def student_grade():
    try:
        mark = int(input("Enter your mark: "))

        if mark > 100 or mark < 0:
            print("Invalid input")

        elif 91 <= mark <= 100:
            print("Your Grade is : O")

        elif 81 <= mark <= 90:
            print("Your Grade is : A")

        elif 71 <= mark <= 80:
            print("Your Grade is : B")

        elif 61 <= mark <= 70:
            print("Your Grade is : C")

        elif 51 <= mark <= 60:
            print("Your Grade is : D")

        else:
            print("You have to reattempt the exam")

    except ValueError:
        print("Please enter a valid number")


student_grade()


def student_average():
    sub1_mark = int(input("Enter mark 1: "))
    sub2_mark = int(input("Enter mark 2: "))
    sub3_mark = int(input("Enter mark 3: "))
    sub4_mark = int(input("Enter mark 4: "))
    sub5_mark = int(input("Enter mark 5: "))

    marks = [sub1_mark, sub2_mark, sub3_mark, sub4_mark, sub5_mark]

    sum_marks = sum(marks)
    len_marks = len(marks)

    mark_average = sum_marks / len_marks

    print("Average Mark is:", mark_average)


student_average()