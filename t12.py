from t11 import Person


class Employee(Person):
    def __init__(self, full_name='', birthyear='', position='', experience=None, salary=None):
        super().__init__(full_name, birthyear)
        self.position = position
        self.experience = int(experience)
        self.salary = int(salary)

    def exp_pos(self):
        if 0 < self.experience < 3:
            exp = 'Junior'
        elif 3 <= self.experience < 6:
            exp = 'Middle'
        elif self.experience >= 6:
            exp = 'Senior'
        return "{} {}".format(exp, self.position)

    def salary_raise(self,amount=0):
        self.salary += amount

    def __str__(self):
        return"{} {}".format(self.__class__, self.full_name)


class ITEmployee(Employee):
    def __init__(self, full_name='', birthyear='', position='', experience=None, salary=None, skills=[]):
        super().__init__(full_name, birthyear, position, experience, salary)
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_skills(self, *skills):
        self.skills.extend(skills)

    def __str__(self):
        return"{} {}".format(self.__class__, self.full_name)


if __name__ == '__main__':
    Igor = Employee('Igor Kalynovskyi', 1987, 'QA', 6, 3000)
    print(Igor.exp_pos())
    print(Igor.salary)
    Igor.salary_raise(1500)
    print(Igor.salary)


    Igor1 = ITEmployee('Igor Kalynovskyi', 1987, 'QA', 6, 3000, [])
    print(Igor1.skills)
    Igor1.add_skill('bicycling')
    print(Igor1.skills)
    Igor1.add_skills('watching movies', 'python', 'poker', 'gaming')
    print(Igor1.skills)

    print(Igor)
    print(Igor1)