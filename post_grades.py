def post_grades(students):
    result = []

    for student in students:
        parts = student.split(' - ')
        student_id = parts[0]
        grades = list(map(float, parts[2].split()))
        average_grade = sum(grades) / len(grades)
        result.append((student_id, average_grade))
    
    
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
    
    return sorted_result



students = [
  'S01 - Student Name A - 95 98.4 92.15', 
  'S02 - Student Name B - 100 96.4 90', 
  'S03 - Student Name C - 84.2 90.5 92.8', 
  'S04 - Student Name D - 80 96.4 88.4'
]


assert post_grades(students) == [('S02',95.47),('S01',95.18),('S03',89.17),('S04',88.27)]