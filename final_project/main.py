"""
INF 360 - Final Project: Main Entry Point
Author: Daniel Obazee
Description: A quiz application that processes computer science questions.

This module serves as the main entry point for the quiz application. It initializes the quiz data, manages the game flow, and handles user interactions while ensuring robust error handling and logging throughout the process.
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