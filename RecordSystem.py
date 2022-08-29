# Exercise 5

def getdate():
    import datetime
    return datetime.datetime.now()


def exercise(PersonName):
    PersonName = PersonName + 'Ex'
    ExerciseFileOfPerson = open(PersonName, 'a+')
    TypeOFExercise = input('Enter the name of Exercise: ')
    NoOfTimesExerciseDone = input(f"No of Times {TypeOFExercise} done:")
    ExerciseFileOfPerson.write(
        str(getdate()) + " " + TypeOFExercise + " " + str(NoOfTimesExerciseDone) + '\n')
    ExerciseFileOfPerson.close()
    return PersonName


def food(PersonName):
    PersonName = PersonName + 'F'
    FoodFileOfPerson = open(PersonName, 'a+')
    NameOfFood = input('Enter your name of food: ')
    NoOfFoodTaken = input(f"No of {NameOfFood} taken:")
    FoodFileOfPerson.write(str(getdate()) + " " +
                           NameOfFood + " " + str(NoOfFoodTaken) + '\n')
    FoodFileOfPerson.close()
    return PersonName


def jim(NameList):
    PersonName = input("Enter the name: ").lower().capitalize()
    if PersonName in NameList:
        job = input(
            'What you want to add? Press "F" to add food record and "E" to add exercise record: ').upper()
        if job == 'F':
            PersonName = food(PersonName)
            print("Record Updated **")
            print(open(PersonName, 'r').read())
        elif job == 'E':
            PersonName = exercise(PersonName)
            print("Record Updated **")
            print(open(PersonName, 'r').read())
        else:
            print("Error: Wrong input!")
    else:
        print(f"""
Enter a correct name, current names in the record {NameList}.
If name is not in the list try creating +it after restarting""")


FileWithNames = open('allnames', 'r')
AllNameList = []
for i in FileWithNames.readlines():
    i = i[:-1]
    AllNameList.append(i)
FileWithNames.close()
print(f'Current user names : {AllNameList}')
ToDo = input("""
What you want to do:
Type A to access existing user
Type N to create new user
Type R to just read your record
> 
""").capitalize()
if ToDo == 'A':
    jim(AllNameList)
elif ToDo == "R":
    Personname = input("Enter the name: ").lower().capitalize()
    if Personname in AllNameList:
        WhichFile = input(
            "Which file you want to access? Press 'E' for Exercise and 'F' for food.")
        if WhichFile == 'E':
            Personname = Personname + 'Ex'
            ReadFile = open(Personname, 'r')
            print(ReadFile.read())
        elif WhichFile == 'F':
            Personname = Personname + 'F'
            ReadFile = open(Personname, 'r')
            print(ReadFile.read())
        else:
            print("Wrong Input!")
    else:
        print("You are not a registered user, please restart and add your name first")
elif ToDo == 'N':
    NewName = input('Enter your name').upper().capitalize()
    if NewName in AllNameList:
        print("User Id already existed!")
    else:
        FileWithNames = open('allnames', 'a+')
        FileWithNames.write(NewName + '\n')
        FileWithNames.close()
        print('User Created , Please start again to access.')
else:
    print("Error: Invalid Input!")
