from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass


class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20


class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.10


class Salesperson(Employee):

    def __init__(self, name, salary, sales):
        super().__init__(name, salary)
        self.sales = sales

    def calculate_bonus(self):
        return self.sales * 0.05


employees = [
    Manager("Alice", 90000),
    Developer("Bob", 75000),
    Salesperson("Charlie", 50000, 200000)
]


for employee in employees:
    bonus = employee.calculate_bonus()

    print(
        f"{employee.name} receives a bonus of "
        f"${bonus:.2f}"
    )


# employee = Employee("John", 50000)
# Error: Employee is an abstract class