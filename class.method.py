class Student:
    total_gpa = 0
    count=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa

        Student.count +=1
        Student.total_gpa +=gpa


    #Instance method
    def get_info(self):
        return f"{self.name},{self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count} "

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.3f}"

Student1 = Student("josef", 3.2)
Student2 = Student("Muse", 2.0)
Student3 = Student("Muhamed", 4.0)


print(Student.get_count())
print(Student.get_average_gpa())





















