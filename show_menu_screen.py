process = ''

def show_menu():
    """show menu function"""
    from start import start_quize
    from add_question import add
    from delete_question import delete
    from sarech_question import sarech
    from statistics import statistic
    from previous_results import previous
    #print("\n \t ========== SMART QUIZ SYSTEM ==========")
   # print(" 1. Start Quiz \n 2. View Previous Results ")
   # print(" 3. Add Question \n 4. Delete Question ")
   # print(" 5. Search Question \n 6. Statistics \n 7. Exit ")


    while True:
        print("\n \t ========== SMART QUIZ SYSTEM ==========")
        print(" 1. Start Quiz \n 2. View Previous Results ")
        print(" 3. Add Question \n 4. Delete Question ")
        print(" 5. Search Question \n 6. Statistics \n 7. Exit ")
        process = input("What would you like to do? ")
        if process == "1":
            start_quize()

        elif process == "2":
            previous()
        elif process == "3":
            add()

        elif process == "4":
            delete()

        elif process == "5":
            sarech()

        elif process == "6":
            statistic()

        elif process == "7":
            break
