"""
    里氏替换原则
"""


# 定义一个员工管理类，包括存储员工的变量，以及计算薪水的方法
class EmployeeManager(object):
    def __init__(self) -> None:
        self.__list_employee = []

    def add_employee(self, employee_):
        self.__list_employee.append(employee_)

    def calculate_total_salary(self):
        return sum(employee.get_salary() for employee in self.__list_employee)


# 定义员工父类，存储员工基本薪水的变量
class Employee(object):
    def __init__(self, base_salary_) -> None:
        self.base_salary: float = base_salary_

    def get_salary(self):
        return self.base_salary


# 定义后端开发类
class Programmer(Employee):
    def __init__(self, base_salary_, bonus_) -> None:
        super().__init__(base_salary_=base_salary_)
        self.bonus: float = bonus_  # 绩效

    def get_salary(self):
        return super().get_salary() + self.bonus


# 定义测试类
class Tester(Employee):
    def __init__(self, base_salary_, bug_count_) -> None:
        super().__init__(base_salary_=base_salary_)
        self.bug_count: int = bug_count_

    def get_salary(self):
        return super().get_salary() + self.bug_count * 50


emp_manager = EmployeeManager()

programmer_1 = Programmer(7000, 3000)
tester_1 = Tester(5000, 50)

emp_manager.add_employee(programmer_1)
emp_manager.add_employee(tester_1)
total_salary = emp_manager.calculate_total_salary()

print(total_salary)
