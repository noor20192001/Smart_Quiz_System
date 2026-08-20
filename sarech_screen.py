import json
from question_screen import id_easy, id_medium, id_hard
easy=[]
medium=[]
hard=[]
all_questions = []
def sarech():
    while True:
        print("If you finish, enter َ'Q'")
        way = input("How do you want to search?ID ,Difficulty level or Keyword inside the question text. ")
        if way =="Q":
            break
        with open("easy.json") as file:
            easy = json.load(file)

        with open("medium.json") as file:
            medium = json.load(file)

        with open("hard.json") as file:
            hard = json.load(file)

        all_questions = easy[:len(id_easy)] + medium[:len(id_medium)] + hard[:len(id_hard)]

        if way.lower() == "id":
            id_ofSarech = input("Enter the question ID: ")
            for question in all_questions:
                if id_ofSarech in question["id"]:
                    print("Question ID: ", question["id"])
                    print("Question: ", question["question"])
                    print("Difficulty:", question["difficulty"])
                    print("Options:")
                    for option in question["options"]:
                        print("\t", option)
                    print("Answer:", question["answer"])


        elif way.lower() == "difficulty level":
            level_ofsarech = input("Enter the level you want to sarech in: ")

            for question in all_questions:
                if level_ofsarech in question["difficulty"]:
                    print("Question ID: ", question["id"])
                    print("Question: ", question["question"])
                    print("Difficulty:", question["difficulty"])
                    print("Options:")
                    for option in question["options"]:
                        print("\t", option)
                    print("Answer:", question["answer"])


        elif way.lower() == "keyword in question":
            keyword_ofsarech = input("Enter the keyword you want to sarech with: ")
            for question in all_questions:
                if keyword_ofsarech.lower().strip() in question["question"].lower():
                    print("Question ID: ", question["id"])
                    print("Question: ", question["question"])
                    print("Difficulty:", question["difficulty"])
                    print("Options:")
                    for option in question["options"]:
                        print("\t", option)
                    print("Answer:", question["answer"])
