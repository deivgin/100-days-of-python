# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuestionBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.last_question = False

    def check_if_last(self):
        return self.question_number == len(self.question_list)

    def check_answer(self, user_input):
        question = self.question_list[self.question_number]
        if question.answer.lower() == user_input:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}")

    def next_question(self):
        if self.check_if_last():
            self.last_question = True
            return

        self.question_number += 1

    def get_user_input(self):
        question_num = self.question_number + 1
        question = self.question_list[self.question_number].text
        user_input = input(f"Q.{question_num}: {question} (True/False): ").lower()

        if user_input not in ["true", "false"]:
            print("Invalid input. Please enter 'True' or 'False'.")
            return self.get_user_input()

        return user_input
