#-------------------------------------------------------------------------
# AUTHOR: Joel Joshy
# FILENAME: decision_tree_2.py
# SPECIFICATION: Decision Tree Algorithm
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for row in dbTraining:
        drow = []
        for i, value in enumerate(row):
            if i == 0: drow.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
            elif i == 1: drow.append(1 if value == 'Myope' else 2)
            elif i == 2: drow.append(1 if value == 'No' else 2)
            elif i == 3: drow.append(1 if value == 'Reduced' else 2)
        X.append(drow)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =

    for row in dbTraining:
       Y.append(1 if row[-1] == 'Yes' else 2)

    #loop your training and test tasks 10 times here
    accuracy = []

    for i in range (10):
       TP = 0
       TN = 0
       FP = 0
       FN = 0
       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       # dbTest =
       dbTest = []
       with open('contact_lens_test.csv', 'r') as csvfile:
           reader = csv.reader(csvfile)
           for i, row in enumerate(reader):
              if i > 0: #skipping the header
                dbTest.append(row)
        
       testData = []
       testClass = []
       i = 0




       for row in dbTest:

           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
           #--> add your Python code here
           drow = []
           for j, value in enumerate(row):
                if j == 0: drow.append(1 if value == 'Young' else 2 if value == 'Prepresbyopic' else 3)
                elif j == 1: drow.append(1 if value == 'Myope' else 2)
                elif j == 2: drow.append(1 if value == 'No' else 2)
                elif j == 3: drow.append(1 if value == 'Reduced' else 2)
           testData.append(drow)

           testClass.append(1 if row[-1] == 'Yes' else 2)

           class_predicted = clf.predict([testData[i]])[0]
           #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
           #--> add your Python code here

           if class_predicted == 1 and testClass[i] == 2:
               FP+=1
           elif class_predicted == 2 and testClass[i] == 1:
               FN+=1
           elif class_predicted == 2 and testClass[i] == 1:
               TN+=1
           else:
               TP+=1
           i+=1
       accuracy.append((TP + TN)/(TP + TN + FP + FN))
            

    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here

    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("Final Accuracy for " + ds + "is ", min(accuracy))



