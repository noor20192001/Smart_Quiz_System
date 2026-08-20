import json
from question_screen import id_easy,id_medium,id_hard
data =[]
score = []
def statistic():
    total_len = len(id_easy) + len(id_medium) + len(id_hard)
    print("The total number of questions", total_len)
    print("The number of questions in easy level", len(id_easy))
    print("The number of questions in medium", len(id_medium))
    print("The number of questions in hard", len(id_hard))

    with open("result.json","r") as file:
        datas = json.load(file)
    all_score = [attemp["score"] for attemp in datas]
    average_score = sum(all_score)/len(all_score)
    max_score = max(all_score)
    print("The average score is: ", average_score)
    print("The maximum score is: ", max_score)
