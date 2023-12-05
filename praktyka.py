user_choice = -1


task = []
task.append("Posprzatac Pokoj")
task.append("Odrobic Lekcje")

def show_task():
    task_index = 0
    for zadania in task:
        print(zadania + " [" + str(task_index) + "]")
        task_index += 1
while user_choice != 5:
    if user_choice == 1:
        show_task()

    if user_choice == 2:
        tasks = input("Wpisz tresc zadania: ")
        task.append(tasks)

    # if user_choice == 3:

    print()    
    print("1. Pokaz Zadania")
    print("2. Dodaj Zadanie")
    print("3. Usun Zadanie")
    print("4. Zapisz Zmiany Do Pliku")
    print("5. Wyjdz")

    user_choice = int(input("Wybierz Liczbe: "))
    print()