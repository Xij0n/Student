class Student:
    def __init__(self, name, age, average_grade):
        self.name = name
        self.age = age
        self.average_grade = average_grade

    # Методы для установки значений свойств класса
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_average_grade(self, average_grade):
        self.average_grade = average_grade

    # Методы для получения значений свойств
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_average_grade(self):
        return self.average_grade

    # Метод для вывода информации о студенте
    def print_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.average_grade}")

    # Метод для подсчета оценки студента
    def evaluate_performance(self):
        if self.average_grade > 8:
            return "Отлично"
        elif 6 <= self.average_grade <= 8:
            return "Хорошо"
        elif 4 <= self.average_grade < 6:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

    # Дополнительный метод для увеличения среднего балла
    def improve_grade(self, increment):
        self.average_grade += increment
        if self.average_grade > 10:
            self.average_grade = 10
        print(f"Средний балл после улучшения: {self.average_grade}")

# Создание объектов класса "Студент"
student1 = Student("Петр Герасимов", 20, 6.3)
student2 = Student("Александр Софронов", 22, 9.5)
student3 = Student("Димтрий Кулебяка", 19, 4.8)
student4 = Student("Наташа Викторовна", 21, 8.3)

# Демонстрация использования объектов
student1.print_info()
print("Оценка:", student1.evaluate_performance())

student2.print_info()
print("Оценка:", student2.evaluate_performance())

student3.print_info()
print("Оценка:", student3.evaluate_performance())

student4.print_info()
print("Оценка:", student4.evaluate_performance())

# Улучшение среднего балла у студента
student4.improve_grade(1.0)
student4.print_info()
print("Оценка:", student4.evaluate_performance())
