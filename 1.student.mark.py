Students = []
Courses = []
Marks = []
Stu_numbs= int(input("Number of students:"))
for i in range (Stu_numbs):
    Informations= [
        int(input("Id:")),
        input("Name:"),
        input("DoB:")
        ]
    Students.append(Informations)
    
Courses_nb = int(input("Number of your courses:"))
for i in range (Courses_nb):
    Course_info = [
        input("Subject ID:"),
        input("Name:")
        ]
    Courses.append(Course_info)

for i in range(len(Courses)):
    print("Enter mark for", Courses[i])

    Course_marks=[]

    for f in range(len(Students)):
        print("Mark for", *Students[f], end = ": ")
        mark= float(input())
        Course_marks.append([Students[0],mark])
    Marks.append([Courses, Course_marks])
                        
Stu_mark_management= {"Stu_info":Students, "Courses":Courses, "Marks":Marks}
print(Stu_mark_management)