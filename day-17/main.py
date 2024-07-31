from data import question_data
from question_model import Question
from question_brain import QuestionBrain


def get_question_list():
    question_list = []

    for question in question_data:
        question_list.append(Question(question["text"], question["answer"]))

    return question_list


def main():
    question_list = get_question_list()
    question_brain = QuestionBrain(question_list)

    while not question_brain.last_question:
        user_input = question_brain.get_user_input()
        question_brain.check_answer(user_input)
        question_brain.next_question()


main()
