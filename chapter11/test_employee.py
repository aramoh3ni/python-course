# import unittest
# from employee import Employee

# class TestEmployee(unittest.TestCase):
#     def setUp(self):
#         firstname = "Joan"
#         lastname = "Doe"
#         self.sallery = 5000
#         self.employee = Employee(firstname, lastname, self.sallery)

#     def test_default_raise(self):
#         self.employee.give_raise()
#         self.assertEqual(self.employee.sallery, self.sallery + 5000)

#     def text_give_custom_raise(self):
#         custom_raise = 10000
#         self.employee.give_raise(custom_raise)
#         self.assertEqual(self.employee.sallery, self.sallery + custom_raise)

# if __name__ == "__main__":
#     unittest.main()