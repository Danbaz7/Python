"""
INF 360 - Final Project: Quiz Box Module
Contains the Question model and QuizBrain logic with robust error handling.
"""
import logging

# Basic logging configuration to capture debug and critical errors in the quiz application.
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Question:
    """Represents a single quiz question."""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    """Manages the flow, scoring, and validation of the quiz."""
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        logging.debug(f"QuizBrain initialized with {len(q_list)} questions.")

    def still_has_questions(self):
        """Checks if there are questions remaining in the list."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieves the next question and validates user input."""
        if not self.question_list:
            logging.critical("Question list is empty! Cannot proceed.")
            return

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        # Input Validation Loop
        valid_input = False
        while not valid_input:
            try:
                user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").strip()
                
                # Check if input is valid
                if user_answer.lower() not in ["true", "false"]:
                    logging.warning(f"Invalid user input received: {user_answer}")

                    raise ValueError("Answers must be given in the True or False format.")
                
                valid_input = True
                self.check_answer(user_answer, current_question.answer)
                
            except ValueError as e:
                # Catching the error to inform the user without crashing the program
                print(f"Error: {e}")
                print("Please try again.")

    def check_answer(self, user_answer, correct_answer):

        """Compares user answer with the correct answer and updates score."""
        logging.debug(f"Checking answer: User said {user_answer}, Correct is {correct_answer}")
        
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")