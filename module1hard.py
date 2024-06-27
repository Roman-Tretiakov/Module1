grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def get_average_grades(grade_list, students_set):
    if len(grade_list) != len(students_set):
        print('Quantity of block of students grades is not equal to quantity of students! Please check!')
        return

    dictionary_with_student_grades = {}
    sorted_students = sorted(students_set)

    for i in range(len(sorted_students)):
        dictionary_with_student_grades.update({sorted_students[i]: sum(grade_list[i]) / len(grade_list[i])})

    return dictionary_with_student_grades


print(get_average_grades(grades, students))
