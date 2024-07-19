import random
#Question to be asked
quiz_data = [
    {
        "question": "Which of the following defines an algorithm?",

        "options": ["A. It is a graphical representation of a program flow", "B. It is the documentation of program logic", "C. It is a list of the sequence of steps required to solve the problem" , "D. none"],
        "answer": "C"
    },
    {
        "question": "Which operator is right-associative?",
        "options": ["A.* ", "B.= ", "C.+ ", "D.% "],
        "answer": "B"
    },
    {
        "question": "Which programming language is often used for data analysis and scientific computing?",
        "options": ["A. JavaScript", "B. Java", "C. Python", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does API stand for in the context of web development?",
        "options": ["A. Application Programming Interface", "B. Advanced Programming Interface", "C. Automated Program Interaction", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of the following code: `print(3 * 'Hello ')`?",
        "options": ["A. Hello Hello Hello Hello", "B. 9", "C. Hello Hello Hello", "D. Syntax Error"],
        "answer": "C"
    },
    {
        "question": "In JavaScript, how do you declare a variable?",
        "options": ["A. var", "B. variable", "C. let", "D. declare"],
        "answer": "A"
    },
    {
        "question": "Which data type in Python is used to represent a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "answer": "C"
    },
    {
        "question": "What is the primary purpose of version control systems like Git?",
        "options": ["A. To write code", "B. To run code", "C. To manage and track changes in code", "D. To execute code"],
        "answer": "C"
    },
    {
        "question": "What is the main advantage of object-oriented programming (OOP)?",
        "options": ["A. Simplicity", "B. Reusability", "C. Procedural nature", "D. No need for functions"],
        "answer": "B"
    },
    {
        "question": "What is the HTTP status code for a successful response?",
        "options": ["A. 200 OK", "B. 404 Not Found", "C. 500 Internal Server Error", "D. 302 Found"],
        "answer": "A"
    },
    {
        "question": "In Python, which library is commonly used for data visualization?",
        "options": ["A. NumPy", "B. Pandas", "C. Matplotlib", "D. TensorFlow"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of a constructor method in object-oriented programming?",
        "options": ["A. To create objects", "B. To destroy objects", "C. To update objects", "D. To copy objects"],
        "answer": "A"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    {
        "question": "What is the result of the following Python code: `3 + '3'`?",
        "options": ["A. 6", "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "C"
    },
    {
        "question": "Which of these is not a core data type?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Class"],
        "answer": "D"
    },
    {
        "question": "Which of the following is a Python tuple?",
        "options": ["A. [1,2,3,4]", "B. (1,2,3,4)", "C. {1,2,3,4}", "D. {}"],
        "answer": "B"
    }
]
#displaying content
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter your answer (A,B,C,D): ").upper()
    if user_answer == question_data["answer"]:
        return True
    else:
        return False
#main body
if __name__=="__main__":
    score=0
    random.shuffle(quiz_data)
    for i in range(1,6):
        print(f'Question {i} of 5')
        if ask_question(quiz_data[i]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {quiz_data[i]['answer']}.\n")

