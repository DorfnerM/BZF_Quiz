import pickle
import random
import os


def import_from_pickle(pickle_file):
    with open(pickle_file, 'rb') as file:
        return pickle.load(file)

def shuffle_answers(answers):
    correct_answer = answers['A']
    shuffled_answers = list(answers.values())
    random.shuffle(shuffled_answers)
    shuffled_dct = {shuffled_answers[0] : 'A', 
                    shuffled_answers[1] : 'B', 
                    shuffled_answers[2] : 'C', 
                    shuffled_answers[3] : 'D'}
    correct_answer = shuffled_dct[correct_answer]
    shuffled_dct = {value: key for key, value in shuffled_dct.items()}

    return shuffled_dct, correct_answer

def ask_question(question_data):
    print(question_data['question'])
    shuffled_answers, correct_answer = shuffle_answers(question_data['answers'])
    
    for key, answer in shuffled_answers.items():
        print(f"{key}. {answer}")
    
    user_input = input("Your answer (A/B/C/D): ").upper()

    return user_input, correct_answer

def quiz(questions):
    correct_answers = 0
    questions_asked = 0

    shuffled_questions = list(questions.items())
    random.shuffle(shuffled_questions)    

    for _, question_data in shuffled_questions:
        user_answer, correct_answer = ask_question(question_data)

        if user_answer == str(correct_answer):
            print("\033[32mCorrect!\033[0m")
            correct_answers += 1
            questions_asked += 1
            print(f"You got {correct_answers} out of {questions_asked} questions correct.\n")
        else:
            questions_asked += 1
            print(f"\033[31mWrong\033[0m. The correct answer is {correct_answer}: {question_data['answers']['A']}")
            print(f"You got {correct_answers} out of {questions_asked} questions correct.\n")
            
    print(f"You got {correct_answers} out of {len(questions)} questions correct.")


pickle_file_path = os.path.join(os.path.dirname(__file__), '2023Pruefungsfragen_BZFII_BZFI.pkl')    
questions = import_from_pickle(pickle_file_path)
quiz(questions)
