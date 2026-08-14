import json
from datetime import datetime
from question import id_hard,id_medium,id_easy
from show_meun_function import show_menu
file_name_result = "result.json"
useranswer = ''
global score
score=0
easy = []
medium = []
hard = []

wrong_answer = 0
precent = 0
def user_answer():
    """Editing the answer that the user enters"""
    global score

    useranswer = input("\t Enter your answer: ")
    if useranswer:
        useranswer = useranswer.upper()
        useranswer = useranswer.lstrip()
        useranswer = useranswer.rstrip()
        return useranswer
    else:
        print("Entering a blank space as an answer is not allowed")
        user_answer()

def start_quize() :
    """Starting the quize function"""
    #from show_meun_function import show_menu
    #global attemp
    global score
    while True:
        score = 0
        print("If you want to exit enter 'Q' in level")
        level = input("\t Available levels: Easy, Medium, Hard \n Enter level: ")
        if level == "Q":
            show_menu()
        num_question = int(input("Enter number of questions you want: "))
        if level == "Easy":
            if num_question > len(id_easy):
                 print("number of questions not allowed")
                 num_question = int(input("Enter again number of questions you want: "))
            with open ("easy.json") as file_object:
                easystart = json.load(file_object)
            for question in easystart[:num_question]:
                print("Question ID: ",question["id"])
                print("Question: ",question["question"])
                print("Difficulty:",question["difficulty"])
                print("Options:")
                for option in question["options"]:
                    print("\t",option)

                edit_answer = user_answer()
                if edit_answer == question["answer"]:
                    print("Correct answer")
                    score =score +1
                else:
                    print("Incorrect answer")


        elif level == "Medium":
             if num_question > len(id_medium):
                print("number of questions not allowed")
                num_question = int(input("Enter number of questions you want: "))
             with open ("medium.json") as file_object:
                 medium = json.load(file_object)
             for question in medium[:num_question]:
                print("Question ID: ", question["id"])
                print("Question: ", question["question"])
                print("Difficulty:", question["difficulty"])
                print("Options:")
                for option in question["options"]:
                    print("\t", option)

                edit_answer = user_answer()
                if edit_answer == question["answer"]:
                    print("Correct answer")
                    score =score+1
                else:
                    print("Incorrect answer")


        else:
            if num_question > len(id_hard):
                print("number of questions not allowed")
                num_question = int(input("Enter number of questions you want: "))
            with open ("hard.json") as file_object:
                hard = json.load(file_object)
            for question in hard[:num_question]:
                print("Question ID: ", question["id"])
                print("Question: ", question["question"])
                print("Difficulty:", question["difficulty"])
                print("Options:")
                for option in question["options"]:
                    print("\t", option)

                edit_answer = user_answer()
                if edit_answer == question["answer"]:
                    print("Correct answer")
                    score = score+1
                else:
                    print("Incorrect answer")


        print("The number of questions you answered",num_question)
        print("The correct answer is",score)
        wrong_answer = num_question - score
        print("The wrong answer is",wrong_answer)
        print("The total score is",score)
        precent  = (score/num_question)*100
        print("Percentage of correct answer",score/num_question*100)
        if precent > 50:
            status = "success"
            print("Status is Successful")
        else:
            status = "failure"
            print("Status is Failed")
        info =[]
        now = datetime.now()
        start_time = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open (file_name_result) as file_object:
                inform = json.load(file_object)
        except FileNotFoundError:
            info.append({ "score": score, "time": start_time, "status": status})
            with open(file_name_result,'w') as file_object:
                json.dump(info,file_object)

        else:
            inform.append({ "score": score, "time": start_time, "status": status})
            with open(file_name_result,'w') as file_object:
                json.dump( inform,file_object)
