import json
import os
global id_easy
global id_medium
global id_hard
global numberofeasy
global numberofmedium
global numberofhard
id_easy =[]
id_medium = []
id_hard = []
def load_qustion(filename,default_list):
    if os.path.exists(filename):
        with open(filename,'r') as file_object:
            return json.load(file_object)

    else:
        with open(filename,'w') as file_object:
            json.dump(default_list,file_object)
            return default_list

default_easy = [{"id": "1.1.", "question": "What's Python?",
                     "options": ["A. Programming Language"," B. Datatbase"," C. Operating System"," D. Browser"],
                     "difficulty":"Easy", "answer":"A"},
            {"id": "1.2.", "question": "What is the correct extension for Python files",
                     "options": ["A. .pt", "B. .pyt", "C. .py", "D. .pyc"],
                     "difficulty":"Easy","answer":"C"},
            {"id": "1.3.", "question": "How do you start writing a comment in Python",
                     "options": ["A. //", "B. #", "C. /*", "D. --"],
                     "difficulty":"Easy","answer":"B"},]

filename_easy = "easy.json"

default_medium =[{"id": "2.1.", "question": "Which function is used to remove leading and trailing whitespace from a string?",
             "options": ["A. strip()", "B. trim()"," C. cut()", "D. len()"],
             "difficulty": "Medium","answer":"A"},
            {"id": "2.2.", "question": " What is the result of the following code: len(['apple', 'banana','cherry'])? ",
             "options": ["A. 1", "B. 2", "C. 3", "D. 15"],
             "difficulty": "Medium","answer":"C"},
            {"id": "2.3.", "question": "What is the output of the following code: print(10 // 3)?",
             "options": ["A. 3.33", "B. 3", "C. 1", "D. 0"],
             "difficulty": "Medium","answer":"B"},]

filename_medium = "medium.json"

default_hard =[{"id": "3.1.", "question": "Which of the following data types is considered immutable? ",
             "options":  ["A. List", "B. Dictionary", "C. Set"," D. Tuple"],
             "difficulty": "Hard","answer":"D"},
            {"id": "3.2.", "question": "What is the keyword used to create a function in Python?",
             "options": ["A. define", "B. func"," C. def"," D. function"],
             "difficulty": "Hard","answer":"C"},
            {"id": "3.3.", "question": "What is the correct way to open a file for reading only in Python?",
             "options": ["A. open(file, 'w')"," B. open(file, 'r')"," C. open(file, 'a')", "D. open(file, 'x')"],
             "difficulty": "Hard","answer":"A"},
            ]

filename_hard = "hard.json"

easy  =load_qustion(filename_easy,default_easy)
medim = load_qustion(filename_medium,default_medium)
hard =load_qustion(filename_hard,default_hard)
id_easy = [q["id"] for q in easy]
id_medium = [q["id"]for q in medim]
id_hard = [q["id"]for q in hard ]
