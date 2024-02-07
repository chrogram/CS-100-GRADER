import csv
import fileIO

while(True):
    
    print("1 - HW")
    print("2 - LAB")
    print("3 - PROJECT")
    print("0 - Exit")
    

    flag = True
    while(flag):
        flag = False
        selection = int(input("Select grading operation: "))
        number = input("Input assignment number in format XX (e.g. 05): ")
        file_name = input("CSV of file to grade: ")
        if(selection == 1):
            try:
                fileIO.importHW(file_name, number)
                print("-------------------")
                print("Graded successfully")
                print("-------------------")
            except:
                print("!!!!!!!!!!!!!!")
                print("File not found")
                print("!!!!!!!!!!!!!!")
                

        elif(selection == 2):
            try:
                fileIO.importLab(file_name, number)
                print("-------------------")
                print("Graded successfully")
                print("-------------------")
            except:
                print("!!!!!!!!!!!!!!")
                print("File not found")
                print("!!!!!!!!!!!!!!")
        elif(selection == 3):
            try:
                fileIO.importProject(file_name, number)
                print("-------------------")
                print("Graded successfully")
                print("-------------------")
            except:
                print("!!!!!!!!!!!!!!")
                print("File not found")
                print("!!!!!!!!!!!!!!")
        elif(selection == 0):
            exit()
        else:
            print("invalid option grading operation")
            flag = True