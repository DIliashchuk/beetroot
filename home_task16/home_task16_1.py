class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"I'm {self.name} and I`m {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} study {subject}"

    def take_exam(self, subject):
        return f"{self.name} take exam {subject}"

class Teachers(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def teach(self, subject):
        return f"{self.employee_id} teach {subject}"

    def evaluate_student(self, student_name, subject, grade):
        return f"{self.name} evaluated {student_name}'s {subject} exam with a grade of {grade}."


person1 = Person('Petro', 12)
print(person1.introduction())

person2 = Teachers("Oleksandra", 44, 256, 2000)
print(person2.__dict__)
print(person2.evaluate_student("Semyon", "Math", 11))
