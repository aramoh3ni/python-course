# class AnonymousSurvey:
#     """Collect annonmouse answer to a survey questions."""

#     def __init__(self, question: str):
#         """Store a quiestion, and prepare to responses."""
#         self.question = question
#         self.responses = []

#     def show_question(self):
#         """Show the survey questions."""
#         return self.question

#     def set_responses(self, new_response: str):
#         """Store a single response to the survey list."""
#         self.responses.append(new_response)

#     def show_result(self):
#         """Show all reponses that have been given."""
#         print("Survey Result")
#         for res in self.responses:
#             print(f"- {res}")