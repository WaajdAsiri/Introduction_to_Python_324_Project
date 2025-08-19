import re
import matplotlib.pyplot as plt

def input_grades():
    sName = input("Enter student name: ")
    sGrade = float(input("Enter student grade: "))
    with open("grades.txt", 'a') as file:
        file.write(f"{sName}: {sGrade}\n")
        file.flush()
    print("Student grade added")

def load_grades():
    file = open("grades.txt", 'r')
    value = file.read()
    pattern = "[0-9]+.?[0-9]*"
    grades = (re.findall(pattern, value))
    grades = list(map(float, grades))
    return grades

def calculate_statistics():
    grades = load_grades()

    sum = 0
    high = 0
    low = 100
    for i in grades:
        sum += float(i)
        if float(i) > high:
            high=float(i)
        if float(i) < low:
            low=float(i)
    avg = sum / len(grades)
    print("Average grade: ", avg)
    print("Highest grade: ", high)
    print("Lowest grade: ", low)

def visualize_grades():
    grades = load_grades()
    print(grades)

    file = open("grades.txt", 'r')
    value = file.read()
    pattern = ("[a-zA-Z]+")
    names = (re.findall(pattern, value))
    print(names)

    plt.hist(grades)
    plt.title("Histogram")
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.show()

    plt.bar(names, grades)
    plt.title("Bar chart")
    plt.xlabel('Students')
    plt.ylabel('Grade')
    plt.ylim(0, 100)
    plt.show()

def display_summary():
    grades = load_grades()
    print("number of students: ", len(grades))
    sum = 0
    passS = 0
    failS = 0
    for i in grades:
        sum += i
        if i >= 60:
            passS += 1
        else:
            failS += 1
    print("average grade: ", sum / len(grades))
    print("students passed:", passS)
    print("students failed:", failS)


print("Welcome to Wajd's grade analyzer, please enter the number for the wanted task")
while True:
    choice = input("Which task would you chose?\n"
                   "1 for input grades\n"
                   "2 for calculate statistics\n"
                   "3 for visualize grades\n"
                   "4 for display summary\n"
                   "5 for exiting the program\n")

    if choice == "1":
        input_grades()
    elif choice == "2":
        calculate_statistics()
    elif choice == "3":
        visualize_grades()
    elif choice == "4":
        display_summary()
    elif choice == "5":
        print("Thank you for using Wajd's grade analyzer. Good bye <3")
        break
    else:
        print("Wrong input! please enter a valid input")
