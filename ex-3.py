print("1. insert a new task")
print("2. remove a task")
print("3. show all existing tasks")
print("4. close the program")
print("\ninserisci un codice: \n")
a=int(input())
tasks=[]
while(a!=4):
    if (a == 1):
        task = input("inserisci una task: ")
        tasks.append(task)
    if (a == 2):
        pos = input("inserisci task da eliminare: ")
        tasks.remove(pos)
    if (a == 3):
        for i in tasks:
            print(tasks[i])
    if (a == 4):
        print()
    a = int(input("\ninserisci un codice: "))

