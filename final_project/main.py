"""
INF 360 - Final Project: Main Entry Point
Author: Daniel Obazee
Description: A quiz application that processes computer science questions.

I,  Daniel Obazee , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
"""
import logging
from data import question_data
from quiz_box import Question, QuizBrain

def main():
    # Logging the start of the application
    logging.info("Quiz application started.\n")
   
    question_bank = []
    
    # Process the list of dictionaries from data.py
    for question in question_data:
        try:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        except KeyError as e:
            logging.critical(f"Data format error: Missing key {e}")
            return

    # Initialize the consolidated Quiz class
    quiz = QuizBrain(question_bank)

    # Main Game Loop
    while quiz.still_has_questions():
        quiz.next_question()

    # Final Output
    print("--- Quiz Completed ---")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    logging.info("Quiz application finished successfully.")

if __name__ == "__main__":
    main()