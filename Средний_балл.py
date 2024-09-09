grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# mm - middle_mark
mm_1 = sum(grades[0])/len(grades[0])
mm_2 = sum(grades[1])/len(grades[1])
mm_3 = sum(grades[2])/len(grades[2])
mm_4 = sum(grades[3])/len(grades[3])
mm_5 = sum(grades[4])/len(grades[4])
grades = [mm_1, mm_2, mm_3, mm_4, mm_5]
# students_list
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
# middle_mark
middle_mark = dict(zip(students, grades))
print(middle_mark)