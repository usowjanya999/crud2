from django.test import TestCase
from app1.models import Employee

class EmployeeTestCase(TestCase):
    def SetUp(self):
        Employee.objects.create(idno=1,name="emp1",salary=1000)
        Employee.objects.create(idno=2,name="emp2",salary=2000)
    def test_Employee_test(self):
        obj1 = Employee.objects.get(idno=1,name="emp1",salary=1000)
        obj2 = Employee.objects.get(idno=2,name="emp2",salary=2000)
        self.assertEqual(obj1.name,"emp1")
        self.assertEqual(obj2.name,"emp2")

