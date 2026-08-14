import json
from question import id_easy,id_medium,id_hard

def add():
    """ add question to database """
    while True:
        print("If you finish adding the questions, enter َ'Q'")
        Id = input("Enter ID for question: ")
        if Id in id_easy:
            print("The ID is already taken")
            Id = input("Enter again ID for question: ")

        elif Id in id_medium:
            print("The ID is already taken")
            Id = input("Enter again ID for question: ")

        elif Id in id_hard:
            print("The ID is already taken")
            Id = input("Enter again ID for question: ")

        if Id.upper() == "Q":
            return
        new_question = input("Enter new question text: ").strip()
        if new_question.upper() == "Q":
            break
        print("Enter the options in the following format, A. option1, B. option2 ...")
        option1= input("Enter option 1: ").strip()
        if option1.upper() == "Q":
            break
        option2 = input("Enter option 2: ").strip()
        if option2.upper() == "Q":
            break
        option3 = input("Enter option 3: ").strip()
        if option3.upper() == "Q":
            break
        option4 = input("Enter option 4: ").strip()
        if option4.upper() == "Q":
            break

        option_newquestion = [option1,option2,option3,option4]

        difficulty = input("Enter difficulty level: ").strip().capitalize()
        if difficulty.upper() == "Q":
            break
        answer_newquestion = input("Enter new answer text: ").strip()
        if answer_newquestion.upper() == "Q":
            break


        the_new_question = {"id":Id,"question":new_question,"options":option_newquestion,
            "difficulty": difficulty,"answer":answer_newquestion}
        if difficulty == "Easy":
            with open("easy.json") as object_file:
                easy = json.load(object_file)
            easy.append(the_new_question)
            id_easy.append(Id)

            with open("easy.json", "w") as object_file:
                json.dump(easy, object_file)

        elif difficulty == "Medium":
            with open("medium.json") as object_file:
                medium = json.load(object_file)
            medium.append(the_new_question)
            id_medium.append(Id)

            with open("medium.json", "w") as object_file:
                json.dump(medium, object_file)

        elif difficulty == "Hard":
            with open("hard.json") as object_file:
                hard = json.load(object_file)
            hard.append(the_new_question)
            id_hard.append(Id)

            with open("hard.json", "w") as object_file:
                json.dump(hard, object_file)