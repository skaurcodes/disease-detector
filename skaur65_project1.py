#Sukhraj Kaur
#TCSS 142 Programming Assignment
#Implement a simple machine-learning algorithm that
#uses a rule-based classifier to predict
#whether or not a particular patient has a coronary heart disease.

linecnt = 0
healthycnt = 0          #Create Counters 
sickcnt = 0              
healthySum = [0] * 14             #Creat Lists that contain 13 indicies
sickSum = [0] * 14
sepVal = [0] * 14

def main():                       # A main function that will be called out at the end that will perform all the functions in a sequence 
    fn = input("training set: ")
    in1 = open(fn, "r") #open the input file
    init(in1)
    print("Total Lines Processed: {}".format(healthycnt + sickcnt))
    print("Total Healthy Count: {}".format(healthycnt))
    print("Total Sick Count: {}".format(sickcnt))
    AverageOfHealthy()
    AverageOfSick()
    SeperateValues()
    in1.seek(0)
    GetAccuracy(in1)
    fm = input("test set: ")    #ask for the test file
    in2 = open(fm, "r")
    WriteToFile(in2)
    in1.close()
    in2.close()
    
def init(in1):   #iniate function splits the the information into data by commas
    global linecnt, healthycnt, sickcnt 
    
    for line in in1: 
        data = line.split(",")
        for index in range(0,14):  #converts non number object into 0
            if data[index] == '?':
                data[index] = 0
        condition = int(data[13])     #if condition reads the diagnosing value (14th attribute)
        if condition == 0:
            healthycnt += 1         #if healthy, increase healthy counter
            AddToHealthy(data)       
        else:
            sickcnt += 1          #if sick, increase the sick counter
            AddToSick(data)

            
    
def AddToHealthy(data):   #if the line is healthy, sum up index by index to the healthySum list
    global healthySum
    for index in range(0,14):
        healthySum[index] += float(data[index])
        
def AddToSick(data):       #if the line is sick, sum up index by index to the sickSum list
    global sickSum
    for index in range(0,14):
        sickSum[index] += float(data[index])

def AverageOfHealthy():
    global healthySum       #this appends the average for healthy back to healthySum List 
    for index in range(0,14):
        healthySum[index] = float(healthySum[index]) / healthycnt
    print("Average of Healthy Patients: {}".format([round(el, 2) for el in healthySum]))
        
def AverageOfSick():  
    global sickSum   #this appends the average for sick back to sickSum List 
    for index in range(0, 14):
        sickSum[index] = float(sickSum[index]) / sickcnt
    print("Average of Sick Patients: {}".format([round(el, 2) for el in sickSum]))
    

def SeperateValues():
    global sepVal     #this appends the median values from healthySum and sickSum to sepVal
    for index in range(0, 14):
        sepVal[index] = (healthySum[index] + sickSum[index]) / 2
    print("Seperation Values: {}".format([round(el, 2) for el in sepVal]))

    #Part 1 Ends
    #Part 2 Begins

    #Classifier compare each line with class seperation value
    #if val in line > val in Seperation values patient is at risk

    #Model accuracy: Percent of Patients at risk without having the last
    #and compare answers with the column.

def GetAccuracy(in1):   
    atRisk = 0  
    for line in in1:
        atRiskCount = 0
        data = line.split(",")
        for index in range(0,13):      #Model accuracy re-reads the input file without the diagnosing value
            if data[index] == '?\n' or data[index] == '?': 
                data[index] = 0
            if float(data[index]) > float(sepVal[index]):   #then compare each line for each patient to the seperation value index by index
                atRiskCount += 1
        if atRiskCount >= 7:                    #if more than or 7 attributes have a value larger than the value in seperation value, the person is at risk.
            atRisk += 1
    print("Accuracy {:.2f}".format(atRisk / sickcnt))  #get accuracy by diving the number of people at risk without 14th attribute by actual number of sick people. 

def WriteToFile(in1):  #this function writes out to the output file from the test file
    outputFile = open("Out.csv", "w")
    outputFile.write("ID,Disease\n")
    atRisk = 0
    countno = 0
    for line in in1:
        atRiskCount = 0
        data = line.split(",")    #splits the the information into data by commas
        for index in range(1,14):
            if data[index] == '?\n' or data[index] == '?': #converts non number object into 0
                data[index] = 0
            if float(data[index]) > float(sepVal[index-1]):
                atRiskCount += 1
        outputFile.write(data[0] + ",")   #for each patient id, the function prints yes if at risk, no if healthy
        if atRiskCount >= 7:
            outputFile.write("yes\n")
            atRisk += 1
        else:
            outputFile.write("no\n")
            countno += 1
    outputFile.close()           
    
main()   #Calls out main
