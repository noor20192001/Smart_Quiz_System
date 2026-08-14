import json
from question import id_easy,id_medium,id_hard
def delete():
    global numberofeasy
    global numberofmedium
    global numberofhard
    while True:
        id_ofdelete= input("Enter the ID of question you want to delete: ")
        print("If you finish delete questions, enter َ'Q'")
        if id_ofdelete == "Q":
            break
        if id_ofdelete not in id_easy:
            if id_ofdelete not in id_medium:
                if id_ofdelete not in id_hard:
                    print("The question you are trying to delete is not exist.")

        elif id_ofdelete in id_easy:
            with open("easy.json") as object:
                easy= json.load(object)
            for question in easy[:len(id_easy)]:
                if question["id"] == id_ofdelete:
                    easy.remove(question)
                    id_easy.remove(id_ofdelete)
                    numberofeasy = len(id_easy)
                with open("easy.json", "w") as object:
                    json.dump(easy, object)

        elif id_ofdelete in id_medium:
            with open("medium.json") as object:
                medium= json.load(object)
            for question in medium[:len(id_medium)]:
                if question["id"] == id_ofdelete:
                    medium.remove(question)
                    id_medium.remove(id_ofdelete)
                    numberofmedium= len(id_medium)
                with open("medium.json", "w") as object:
                    json.dump(medium, object)


        else:
            with open("hard.json") as object:
                hard= json.load(object)
            for question in hard[:len(id_hard)]:
                if question["id"] == id_ofdelete:
                    hard.remove(question)
                    id_hard.remove(id_ofdelete)
                    numberofhard= len(id_hard)
                with open("hard.json", "w") as object:
                    json.dump(hard, object)