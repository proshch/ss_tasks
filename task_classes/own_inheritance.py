"""Module for classes structure"""

class Persons:
    """A class used to represent personal info"""

    def __init__(self, first, last, age):
        """Parameters:
            first (str): The first name of person
            last (str): The last name of person
            age (int): Age of person
        """
    @property
    def full_name(self):
        """Get full name of Person"""

        return self.first + ' ' + self.last

    @full_name.setter
    def full_name(self, name):
        """Set full name of person"""

        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        """Delete full name of person"""

        print('Delete name!')
        self.first = ''
        self.last = ''

    def __repr__(self):
        return 'Person({}, {})'.format(self.full_name, self.age)

    def __str__(self):
        return '{} - {} years old'.format(self.full_name, self.age)

class Teachers(Persons):
    """A class used to represent groups info"""

    def __init__(self, first, last, age, subject, salary):
        """Parameters:
            first (str): The first name of person
            last (str): The last name of person
            age (int) Age of person
            subject (str): Subject name
            salary (float): Salary
        """
        super().__init__(first, last, age)
        self.subject = subject
        self.salary = salary

    @classmethod
    def set_raise_amount(cls, amount):
        """Method to set raise amount

        Parametr:
            amount (float): Percents (1.05 = 5%)
        """

        cls.raise_amount = amount

    def raise_salary(self):
        """Method to raise salary of teacher"""

        self.salary = int(self.raise_amount * self.salary)

    def __repr__(self):
        return 'Teacher({}, {}, {}, {})'.format(self.full_name,
                                                self.age,
                                                self.subject,
                                                self.salary)

    def __str__(self):
        return '{} - {} years old. Subject - {}. Salary - {}'.format(self.full_name,
                                                                     self.age,
                                                                     self.subject,
                                                                     self.salary)

class PrivateTeachers(Teachers):
    """A class to represent private teacher info"""

    def __init__(self, first, last, age, subject, salary, pay_per_lesson):
        """Parameters:
            first (str): The first name of person
            last (str): The last name of person
            age (int): Age of person
            subject (str): Subject name
            salary (float): Salary
            pay_per_lesson (int): Cost of one lesson
        """

        super().__init__(first, last, age, subject, salary)
        self.pay_per_lesson = pay_per_lesson

    def num_of_lessons(self):
        """Method to get number of lessons per month"""

        return int(self.salary / self.pay_per_lesson)

    def set_ppl(self, pay):
        """Method to set new pay for one lesson

        Parametr:
            pay (int): Cost of one lesson
        """
        self.pay_per_lesson = pay

    def __repr__(self):
        return 'PrivateTeacher({}, {}, {}, {}, {})'.format(self.full_name,
                                                           self.age,
                                                           self.subject,
                                                           self.salary,
                                                           self.pay_per_lesson)

    def __str__(self):
        return '{} - {} years old. Subject - {}. Salary - {}. Per lesson - {}'.format(self.full_name,
                                                                                      self.age,
                                                                                      self.subject,
                                                                                      self.salary,
                                                                                      self.pay_per_lesson)

