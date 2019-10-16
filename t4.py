import unittest
from t12 import ITEmployee

# class Employee(Person):
#     def __init__(self, full_name='', birthyear='', position='', experience=None, salary=None):
#         super().__init__(full_name, birthyear)
#         self.position = position
#         self.experience = int(experience)
#         self.salary = int(salary)
#
#     def exp_pos(self):
#         if 0 < self.experience < 3:
#             exp = 'Junior'
#         elif 3 <= self.experience < 6:
#             exp = 'Middle'
#         elif self.experience >= 6:
#             exp = 'Senior'
#         return "{} {}".format(exp, self.position)
#
#     def salary_raise(self,amount=0):
#         self.salary += amount
#     def __str__(self):
#         return"{} {}".format(self.__class__, self.full_name)
#
#
# class ITEmployee(Employee):
#     def __init__(self, full_name='', birthyear='', position='', experience=None, salary=None, skills=[]):
#         super().__init__(full_name, birthyear, position, experience, salary)
#         self.skills = skills
#
#     def add_skill(self, skill):
#         self.skills.append(skill)
#
#     def add_skills(self, *skills):
#         self.skills.extend(skills)

#     def __str__(self):
#         return"{} {}".format(self.__class__, self.full_name)

class TestITEmployee(unittest.TestCase):
    def testITEmployeeInitialValuesAreSetCorrectly(self):
        obj = ITEmployee('Igor Kalynovskyi', 1987, 'QA', 6, 3000, [])
        self.assertEqual(obj.full_name, 'Igor Kalynovskyi')         # есть ли смысл в таких проверках? По сути проверяет
        self.assertEqual(obj.birthyear, 1987)        # как работает конструктор пайтона
        self.assertEqual(obj.position, 'QA')
        self.assertEqual(obj.experience, 6)
        self.assertEqual(obj.salary, 3000)
        self.assertEqual(obj.skills, [])


    def testITEmployeeSalaryRaise(self):
        obj = ITEmployee('Igor Kalynovskyi', 1987, 'QA', 6, 3000, [])
        obj.salary_raise(999)
        self.assertEqual(obj.salary, 3999)

    def testITEmployeeAddSkill(self):
        obj = ITEmployee('Igor Kalynovskyi', 1987, 'QA', 6, 3000, [])
        obj.add_skill('poker')
        self.assertEqual(obj.skills, ['poker'])

    def testITEmployeeAddSkills(self):
        obj = ITEmployee('Igor Kalynovskyi', 1987, 'QA', 6, 3000, ['poker', 'polupoker'])
        obj.add_skills('bakkara', 'ruler', 'blackjack')
        self.assertEqual(obj.skills, ['poker', 'polupoker', 'bakkara', 'ruler', 'blackjack'])

    def testITEmployeeAddSkillsOrder(self):             #туповатая проверка, т.к. скиллз это лист
        obj = ITEmployee('Igor Kalynovskyi', 1987, 'QA', 6, 3000, ['poker', 'polupoker'])
        obj.add_skills('bakkara', 'ruler', 'blackjack')
        self.assertNotEqual(obj.skills, ['ruler', 'blackjack', 'polupoker', 'poker', 'bakkara'])


if __name__ == '__main__':
     unittest.main()
