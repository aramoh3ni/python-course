# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousServy"""

#     def setUp(self):
#         """Create a survey and a set of reponses for use in all test methods."""
#         question = "How to become progammer?"
#         self.my_survey = AnonymousSurvey(question)
#         self.new_responses = [
#             "There is some response.",
#             "Learn and code every day.",
#             "There will be some response."
#         ]

#     def test_store_single_response(self):
#         """Test that a single respnse is stored properly."""

#         self.my_survey.set_responses(self.new_responses[0])
#         self.assertIn(self.new_responses[0], self.my_survey.responses)

#     def test_store_three_response(self):
#         """Test that a three respnse is stored properly."""

#         for res in self.new_responses:
#             self.my_survey.set_responses(res)

#         for reses in self.new_responses:
#             self.assertIn(reses, self.my_survey.responses)

# if __name__ == "__main__":
#     unittest.main()