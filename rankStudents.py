# The name for input of the program : [('Faza', 990) , ('Figo' , 890) , ('Indah' , 600) , ('Farhan', 700)]

import random
import operator

def studentDetail():
    print("Enter the number of students :")
    numberStudents = int(input())
    listOfRecords = {}
    for student in range(0, numberStudents):
        print("Name of Students : ")
        names_ = input()
        print("Mark score that you have : ")
        marks_ = int(input())
        listOfRecords[names_] = marks_
    return listOfRecords
    print()

def studentRanks(listOfRecords):
        try:
            sortedlistOfRecords = sorted(listOfRecords.items(), key = operator.itemgetter(1), reverse = True)
            print()
            print(sortedlistOfRecords)
            print("{} has secured first position , with score mark {}".format(sortedlistOfRecords[0][0], sortedlistOfRecords[0][1]))
            print("{} has secured second position , with score mark {}".format(sortedlistOfRecords[1][0], sortedlistOfRecords[1][1]))
            print("{} has secured third position , with score mark {}".format(sortedlistOfRecords[2][0], sortedlistOfRecords[2][1]))
            return sortedlistOfRecords
        except IndexError:
                print("The input was invalid. Please Try Again")
                quit()

def studentRewards(sortedlistOfRecords, rewards):
    print()
    print("{} received a cash reward ${}".format(sortedlistOfRecords[0][0], rewards[0]))
    print("{} received a cash reward ${}".format(sortedlistOfRecords[1][0], rewards[1]))
    print("{} received a cash reward ${}".format(sortedlistOfRecords[2][0], rewards[2]))
    print()


def lottery(studentRewards , ticket):
    print()
    random.shuffle(sortedlistOfRecords)
    for winner in sortedlistOfRecords:
                print("The winner of the lottery is {} , Congratulations you've got a trip to {}".format(sortedlistOfRecords[0][0], ticket))
    print()

def appreciation(sortedlistOfRecords):
    for record in sortedlistOfRecords:
        if record[1] >= 950:
            print("Congratulations {} on great scoring! which is {} marks".format(record[0] , record[1]))
        else:
            break



listOfRecords = studentDetail()
sortedlistOfRecords = studentRanks(listOfRecords)
rewards = (500, 300, 100)
ticket = "Silicon Valley"
studentRewards(sortedlistOfRecords , rewards)
appreciation(sortedlistOfRecords)
lottery(sortedlistOfRecords , ticket)
