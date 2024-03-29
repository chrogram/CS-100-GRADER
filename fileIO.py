import csv

# imports your students found in students.txt
def importStudents(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    lines = content.split('\n')
    return lines

def importLab(filename, NUM):

    temp = importStudents("students.txt")
    students = []

    for i in temp:
        students.append(i+"@crimson.ua.edu")
    header = []
    grades = []
    filename = "toGrade/"+filename

    #find 01supesupport_previewuser
    dumbIndex = ""
    try:
        dumbIndex = students.index("01supesupport_previewuser@crimson.ua.edu")
    except:
        print("error")

    with open(filename, newline='') as section2:
        reader = csv.reader(section2, delimiter=',')
        firstRow = True
        index = 0
        for row in reader:
            # removes header
            if(firstRow == True):
                header.append(row[0])
                header.append(row[1])
                header.append(row[2])
                header.append(row[4])
                firstRow = False
            
            # checks if student is in your section
            elif(row[2].lower() in students):
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                temp.append(row[4])
                grades.append(temp)
                index += 1

    # adds space for supestore user   
    if(dumbIndex != ""):
        grades.insert(dumbIndex-1, [])         

    # adds header to top (optional)
    # grades.insert(0, header)

    #write grades to new csv for copy pasting
    with open('LAB/'+''+'LAB'+str(NUM)+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in grades:
            spamwriter.writerow(row)

def importHW(filename, NUM):

    temp = importStudents("students.txt")
    students = []

    for i in temp:
        students.append(i+"@crimson.ua.edu")
    header = []
    grades = []
    filename = "toGrade/"+filename

    #find 01supesupport_previewuser
    dumbIndex = -1;
    try:
        dumbIndex = students.index("01supesupport_previewuser@crimson.ua.edu")
    except:
        pass

    with open(filename, newline='') as section2:
        reader = csv.reader(section2, delimiter=',')
        firstRow = True
        index = 0
        for row in reader:
            # removes header
            if(firstRow == True):
                header.append(row[0])
                header.append(row[1])
                header.append(row[2])
                header.append(row[4])
                firstRow = False
            
            # checks if student is in your section
            elif(row[2].lower() in students):
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                temp.append(row[4])
                grades.append(temp)
                index += 1

    for percent in grades:
        if(float(percent[3]) >= 70):
            percent[3] = 100
        elif(float(percent[3]) >= 60):
            percent[3] = 90
        elif(float(percent[3]) >= 50):
            percent[3] = 80

    # adds space for supestore user     
    if(dumbIndex != -1):
        grades.insert(dumbIndex-1, [])

    # adds header to top (optional)
    #grades.insert(0, header)

    #write grades to new csv for copy pasting
    with open('HW/'+''+'HW'+str(NUM)+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in grades:
            spamwriter.writerow(row)

def importProject(filename, NUM):

    temp = importStudents("students.txt")
    students = []

    for i in temp:
        students.append(i+"@crimson.ua.edu")
    header = []
    grades = []
    filename = "toGrade/"+filename

    #find 01supesupport_previewuser
    dumbIndex = ""
    try:
        dumbIndex = students.index("01supesupport_previewuser@crimson.ua.edu")
    except:
        print("error")

    with open(filename, newline='') as section2:
        reader = csv.reader(section2, delimiter=',')
        firstRow = True
        index = 0
        for row in reader:
            # removes header
            if(firstRow == True):
                header.append(row[0])
                header.append(row[1])
                header.append(row[2])
                header.append(row[4])
                firstRow = False
            
            # checks if student is in your section
            elif(row[2].lower() in students):
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                temp.append(row[4])
                grades.append(temp)
                index += 1

    # adds space for supestore user   
    if(dumbIndex != ""):
        grades.insert(dumbIndex-1, [])         

    # adds header to top (optional)
    # grades.insert(0, header)

    #write grades to new csv for copy pasting
    with open('PROJECT/'+''+'PROJECT'+str(NUM)+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in grades:
            spamwriter.writerow(row)

def importExam(filename, NUM):

    temp = importStudents("students.txt")
    students = []

    for i in temp:
        students.append(i+"@crimson.ua.edu")
    header = []
    grades = []
    filename = "toGrade/"+filename

    #find 01supesupport_previewuser
    dumbIndex = ""
    try:
        dumbIndex = students.index("01supesupport_previewuser@crimson.ua.edu")
    except:
        print("error")

    with open(filename, newline='') as section2:
        reader = csv.reader(section2, delimiter=',')
        firstRow = True
        index = 0
        for row in reader:
            # removes header
            if(firstRow == True):
                header.append(row[0])
                header.append(row[1])
                header.append(row[2])
                header.append(row[4])
                firstRow = False
            
            # checks if student is in your section
            elif(row[2].lower() in students):
                temp = []
                temp.append(row[0])
                temp.append(row[1])
                temp.append(row[2])
                temp.append(row[5])
                grades.append(temp)
                index += 1

    # adds space for supestore user   
    if(dumbIndex != ""):
        grades.insert(dumbIndex-1, [])
    # print(grades)         
    for percent in grades:
        if(len(percent) > 0):
            if(float(percent[3]) >= 100):
                percent[3] = '100'
            
    # adds header to top (optional)
    # grades.insert(0, header)

    #write grades to new csv for copy pasting
    with open('EXAM/'+''+'EXAM'+str(NUM)+'.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in grades:
            spamwriter.writerow(row)
            
