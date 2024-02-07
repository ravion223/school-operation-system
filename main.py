import django_setup

from school_operation_sys.models import Class, Subject, Teacher, Student


def add_class_to_db(class_name):
    clas = Class(
        class_name = class_name
    )
    clas.save()
    
    return clas


def add_subject_to_db(subject_name):
    subject = Subject(
        subject_name = subject_name
    )
    subject.save()

    return subject


def add_teacher_to_db(teachers_name, teachers_surname):
    teacher = Teacher(
        teachers_name = teachers_name,
        teachers_surname = teachers_surname
    )
    teacher.save()

    return teacher


def add_student_to_db(students_name, students_surname):
    student = Student(
        students_name = students_name,
        students_surname = students_surname
    )
    student.save()

    return student


def sign_student_on_class(student_id, class_id):
    student = Student.objects.get(id = student_id)
    clas = Class.objects.get(id = class_id)
    student.classes.add(clas)


def specialize_teacher_to_current_subject(teacher_id, subject_id):
    teacher = Teacher.objects.get(id = teacher_id)
    subject = Subject.objects.get(id = subject_id)
    teacher.subject.add(subject)

def main():
    while True:
        question = int(input("Register new class - 1\nAdd new subject - 2\nRegister new teacher - 3\nRegister new student - 4\nSign student to new class - 5\nSpecialize teacher with a subject - 6\nExit - 0\n"))

        match question:
            case 1:
                class_name = input("Enter name of class:")
                print(add_class_to_db(class_name))
            
            case 2:
                subject_name = input("Enter name of subject:")
                print(add_subject_to_db(subject_name))

            case 3:
                teachers_name = input("Enter teacher's name:")
                teachers_surname = input("Enter teacher's surname:")
                print(add_teacher_to_db(teachers_name, teachers_surname))

            case 4:
                students_name = input("Enter student's name:")
                students_surname = input("Enter student's surname:")
                print(add_student_to_db(students_name, students_surname))

            case 5:
                student_id = input("Enter student's id:")
                class_id = input("Enter class's id:")
                print(sign_student_on_class(student_id, class_id))

            case 6:
                teacher_id = input("Enter teacher's id:")
                subject_id = input("Enter subject's id:")
                print(specialize_teacher_to_current_subject(teacher_id, subject_id))

            case 0:
                break




if __name__ == "__main__":
    main()