import json
info = []
def previous():
    global attemp
    with open ("result.json","r") as f:
        data = json.load(f)
        print("The number of previous attempts is", len(data))
    for dat in data:
        print("Score is",dat["score"])
        print("The date of attempt is",dat["time"])