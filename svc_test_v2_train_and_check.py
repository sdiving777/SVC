from sklearn import svm
import random
import sys
import joblib



# learning sample
fF = open("svc_v2_train_file.txt","r") 

X_arr_train = []
Y_arr_train = []

for sLine in fF:
    arrTmp = sLine.split(";")
    arrTmp.pop(-1) 

    X_arr_train.append(int(arrTmp[0]))
    
    arrY = []
    for i in range(1,len(arrTmp)):
        arrY.append(int(arrTmp[i]))

    Y_arr_train.append(arrY)
    
fF.close()

clf = svm.SVC(kernel='poly',degree=5)
clf.fit(Y_arr_train,X_arr_train)

# check on learning sample
arr_result = clf.predict(Y_arr_train)
                              
iOKCntr = 0
iFlCntr = 0
for i in range(len(arr_result)):
    if (arr_result[i]==X_arr_train[i]):
        #print(" - OK")
        iOKCntr += 1
    else:
        #print(" - FAIL")
        iFlCntr += 1
print("check on learning sample (Good/Bad):",str(iOKCntr)+"/"+str(iFlCntr))
    
    
# check on test sample   
fF = open("svc_v2_test_file.txt","r") 

arr_arr_Y = []
arr_right_answers = []

for sLine in fF:
    arrTmp = sLine.split(";")
    arrTmp.pop(-1) 

    arr_right_answers.append(int(arrTmp[0]))
        
    arrY = []
    for i in range(1,len(arrTmp)):
        arrY.append(int(arrTmp[i]))
    
    arr_arr_Y.append(arrY)
    
fF.close()

arr_result = clf.predict(arr_arr_Y)
                              
iOKCntr = 0
iFlCntr = 0
for i in range(len(arr_right_answers)):
    if (arr_result[i]==arr_right_answers[i]):
        #print(" - OK")
        iOKCntr += 1
    else:
        #print(" - FAIL")
        iFlCntr += 1

print("check on test sample (Good/Bad):",str(iOKCntr)+"/"+str(iFlCntr))

