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
            {"id": "1.2.", "question": "What's the oop?",
                     "options": ["A. Programming Language"," B. Datatbase"," C. Operating System"," D. Browser"],
                     "difficulty":"Easy","answer":"A"},
            {"id": "1.3.", "question": "What's the use of the set function?",
                     "options": ["A. Programming Language"," B. Datatbase"," C. Operating System"," D. Browser"],
                     "difficulty":"Easy","answer":"A"},]

filename_easy = "easy.json"

default_medium =[{"id": "2.1.", "question": "What's the use of the pop function?",
             "options": ["A. Programming Language", "B. Datatbase", "C. Operating System", "D. Browser"],
             "difficulty": "Medium","answer":"A"},
            {"id": "2.2.", "question": "What's the use of the pop function?",
             "options": ["A. Programming Language", "B. Datatbase", "C. Operating System", "D. Browser"],
             "difficulty": "Medium","answer":"A"},
            {"id": "2.3.", "question": "What's the use of the pop function?",
             "options": ["A. Programming Language", "B. Datatbase", "C. Operating System", "D. Browser"],
             "difficulty": "Medium","answer":"A"},]

filename_medium = "medium.json"

default_hard =[{"id": "3.1.", "question": "What's the use of the set function?",
             "options": ["A. Programming Language", "B. Datatbase", "C. Operating System", "D. Browser"],
             "difficulty": "Hard","answer":"A"},
            {"id": "3.2.", "question": "What's the use of the set function?",
             "options": ["A. Programming Language", "B. Datatbase", "C. Operating System", "D. Browser"],
             "difficulty": "Hard","answer":"A"},
            {"id": "3.3.", "question": "What's the use of the set function?",
             "options": ["A. Programming Language", "B. Datatbase", "C. Operating System", "D. Browser"],
             "difficulty": "Hard","answer":"A"},
            ]

filename_hard = "hard.json"

easy  =load_qustion(filename_easy,default_easy)
medim = load_qustion(filename_medium,default_medium)
hard =load_qustion(filename_hard,default_hard)
id_easy = [q["id"] for q in easy]
id_medium = [q["id"]for q in medim]
id_hard = [q["id"]for q in hard ]